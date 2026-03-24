import cv2
import numpy as np
# Load the image
img = cv2.imread('test_image1.jpg')
img = cv2.resize(img, (600, 700))  # Resize the image to 600x700 pixels
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply median blur to reduce noise
gray = cv2.medianBlur(gray, 5)
# Detect edges using adaptive thresholding
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# Convert the image to color
color = cv2.bilateralFilter(img, 9, 300, 300)
# Combine the color image with the edges mask
cartoon = cv2.bitwise_and(color, color, mask=edges)
# Display the cartoon image

cv2.imshow("Cartoon Rendering", cartoon)
cv2.moveWindow("Cartoon Rendering", 200, 70)  # Move the window to a specific position
cv2.waitKey(0)
cv2.destroyAllWindows() 
