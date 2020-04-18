import numpy as np
import cv2
import random

img = cv2.imread("fuzzy.png",1)
cv2.imshow("Original", img)

bw = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(bw, (3,3),0)
cv2.imshow("Blurred", blur)
thresh = cv2.adaptiveThreshold(blur , 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("Binary", thresh)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

filtered = []

for c in contours:
    if cv2.contourArea(c) < 1000:continue
    filtered.append(c)

print(len(filtered))

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')

for c in filtered:
    col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    cv2.drawContours(objects, [c], -1, col, -1)
    print(cv2.contourArea(c), cv2.arcLength(c, True))

cv2.imshow("Final", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
