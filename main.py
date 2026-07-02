
import cv2 as cv
# image = cv.imread("./Resources/Photos/cat.jpg")
# cv.imshow('cat', image)
# cv.waitKey(0)
# cv.destroyAllWindows()
video = cv.VideoCapture('./Resources/Videos/dog.mp4')
while True:
    isTrue, frame = video.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()