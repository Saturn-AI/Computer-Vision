import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import os

# Read the image
img = cv2.imread('carbd1.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save grayscale image
cv2.imwrite('gray_image.jpg', gray)

# Noise removal
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(bfilter, 80, 400)    # Perform Edge detection

# Save edged image
cv2.imwrite('edged_image.jpg', edged)

# Find contours
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
location = None

for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

# Draw contours
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

# Save masked image
cv2.imwrite('masked_image.jpg', new_image)

# Crop image
(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray[x1:x2+1, y1:y2+1]

# Save cropped image
cv2.imwrite('cropped_image.jpg', cropped_image)

# Read text using EasyOCR
reader = easyocr.Reader( ['bn','en'] )
result = reader.readtext(cropped_image)
text = (result[0][-2]+result[1][-2])

print("Detected text:", text)
