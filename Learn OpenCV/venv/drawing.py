import os

import cv2


img = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))

print(img.shape)

# line
cv2.line(img, (70, 100), (220, 320), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (150, 250), (310, 410), (0, 0, 255), -1)

#circle
cv2.circle(img, (560, 140), 50, (255, 0, 0), 5)

#text
cv2.putText(img, 'Hey you!', (350, 340), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)

cv2.imshow('img', img)
cv2.waitKey(0)