"""
Author: Peter Idoko

Date: 2025-01-16

Purpose: Program that uploads an image using OpenCV,
displays the image, resizes the image, displays the resized image,
rotates the resized image, and displays the rotated image.
"""

# Import OpenCV, requests, os and matplotlib modules
import cv2 as cv # For clarity
import requests # For fetching urls
import os # For interacting with the Google Collab OS
import matplotlib.pyplot as plt

# URL of the image
url = "https://raw.githubusercontent.com/pidoko/CS5330/refs/heads/main/15.JPG"

# Fetch the image from the Github url using requests
# Requests offers more intuitive use than urllib.requests
response = requests.get(url)

# Check HTTP response from server
if response.status_code != 200:
  raise Exception("Fetching file from Github unsuccessful!")

# Save the file in the Google Collab temp environment
image_path = "15.jpg"
# Open using write mode, then save in binary mode, and return file object
with open(image_path, "wb") as picture:
  picture.write(response.content)

# Check if the save is successful
if not os.path.exists(image_path):
  raise FileNotFoundError("The image could not be saved on Google Collab")

# Load the image in Google Collab
image = cv.imread(image_path)

# Check if the image was loaded correctly
if image is None:
  raise ValueError("The image could not be loaded on Google Collab")

# Function to dynamically display an image using matplotlib
def show_image(pic, title):
  # Scale the picture's width and height from pixels to inches
  # for figsize using a dpi of 100
  fig_width = pic.shape[1] / 100
  fig_height = pic.shape[0] / 100
  plt.figure(figsize=(fig_width, fig_height))
  # Convert image from BGR format to RGB for matplotlib
  plt.imshow(cv.cvtColor(pic, cv.COLOR_BGR2RGB))
  plt.title(title)
  # x and y axis need not be shown for this image
  plt.axis('off')
  plt.show()

# Get the loaded image's height and width
original_height, original_width = image.shape[:2]

# Show the image
show_image(image, f"Github Image! ({original_width} X {original_height})")

# While maintaining aspect ratio, resize to height of 300 pixels
aspect_ratio = original_width / original_height
target_height = 300
new_width = int(target_height * aspect_ratio)
resized_image = cv.resize(image, (new_width, target_height),
                          interpolation=cv.INTER_AREA)

# Show the resized image
show_image(resized_image,
           f"Resized Github Image! ({new_width} X {target_height})")

# Rotate the image upside down
rotated_image = cv.rotate(resized_image, cv.ROTATE_180)

# Show the rotated and resized image
show_image(rotated_image,
           f"Rotated Github Image! ({new_width} X {target_height})")
