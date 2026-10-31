import cv2
import mediapipe as mp


# read image
img_path = './data/testImage.png'

img = cv2.imread(img_path)

# detect faces
mp_face_detection =  mp.solutions.face_detection

with mp.solutions.face_detection(min_detection_confidence=0.5, model_selection=0)

# blur faces

# save image