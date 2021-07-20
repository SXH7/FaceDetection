import cv2 as cv

img = cv.imread('C:/Users/shash/OneDrive/Pictures/Tim/tim (2).jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

har_cascade = cv.CascadeClassifier('harcascadeFace.xml')
face_rect = har_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)
print('number of faces found = '+ str(len(face_rect)))



for(x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), thickness=2)

cv.imshow('dected', img)

cv.waitKey(0)
