import argparse
import cv2
import imutils
import numpy as np
from transform import four_point_transform
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image to be scanned")
args = vars(ap.parse_args())

# Recieving and resizing the image
image = cv2.imread(args["image"])
if image is None:
    print(f"Error: Unable to read image file '{args['image']}'")
    exit(1)
ratio = image.shape[0] / 500
orig = image.copy()
image = imutils.resize(image,height = 500) # Resizing to speed up the edge detection process

# grayscaling the image and doing edge detection

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayblur = cv2.GaussianBlur(gray, (5,5), 0) # Gaussian blurring removes high frequency noise
edged = cv2.Canny(grayblur, 75, 200) # Canny edge detection

# Showing org image and edge detected image

cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.imshow("Grayblur", grayblur)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()


# finding contours

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:5]

# Add this after finding contours to check if we actually found the document
screenCnt = None  # Initialize as None
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

# Add error checking
if screenCnt is None:
    print("No document boundaries detected. Please try with better lighting or contrast.")
    exit(1)

# Add debugging output to see the contours
print(f"Number of contours found: {len(cnts)}")
print(f"Points detected: {screenCnt.reshape(4, 2)}")

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Ordering the points and applying perspective transform
pts = screenCnt.reshape(4, 2)
pts = pts * ratio
warped = four_point_transform(orig, pts)
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grayscaling the warped image
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

# Thresholding the image
thresh = cv2.threshold(warped, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Showing the thresholded image
cv2.imshow("Thresholded", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()







