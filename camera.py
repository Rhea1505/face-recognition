import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassufier("haarcascade_frontalface_alt.xml")

while True: