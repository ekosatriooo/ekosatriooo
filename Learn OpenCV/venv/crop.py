# crop
import os

import cv2


img = cv2.imread(os.path.join('.', 'data', 'dogs.jpg'))

print(img.shape)

cropped_img = img[200:780, 100:650]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
