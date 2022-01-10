import cv2
import numpy as np


#########################################
wCam, hCam = 640, 480
#########################################
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(10, 150)
cap.set(cv2.CAP_PROP_FPS, 60)

# tracker = cv2.TrackerMOSSE_create()  ->  OLD
# tracker = cv2.legacy.TrackerMOSSE_create()  # NOW AVAILABLE
tracker = cv2.legacy.TrackerKCF_create()
ret, frame = cap.read()
boundingBox = cv2.selectROI('Tracking', frame, False)
tracker.init(frame, boundingBox)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 3, 1)
    cv2.putText(img, 'Tracking', (15, 65), cv2.FONT_ITALIC, 1.2, (0, 255, 0), 2)
    cv2.circle(img, ((x+x+w)//2, (y+y+h)//2), 5, (0, 255, 0), cv2.FILLED)
    return img


while True:
    timer = cv2.getTickCount()
    ret, frame = cap.read()

    ret, boundingBox = tracker.update(frame)

    if ret:
        frame = drawBox(frame, boundingBox)
    else:
        cv2.putText(frame, 'Lost', (15, 65), cv2.FONT_ITALIC, 1.2, (255, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(frame, f'FPS: {int(fps)}', (15, 35), cv2.FONT_ITALIC, 1.2, (255, 0, 255), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        cap.release()
        cv2.destroyAllWindows()
        break














