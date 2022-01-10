import cv2
import os
import time
from datetime import datetime


##################################################
cap = cv2.VideoCapture(0)
cap.set(10, 100)
all_class = []
now_class = ''
PATH = './images'
if not os.path.exists(PATH):
    os.mkdir(PATH)
PHOTO_NUM = 20
IMG_SIZE = (640, 480)
##################################################
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M")
print(dt_string)


if __name__ == "__main__":
    # global now_class
    while True:
        now_class = str(input("Input Class: "))
        all_class.append(now_class)
        if not os.path.exists(f'{PATH}/{now_class}'):
            os.mkdir(f'{PATH}/{now_class}')
        count = 0
        while not count >= PHOTO_NUM:
            ret, frame = cap.read()
            cv2.imshow('Frame', frame)
            time.sleep(2)
            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y_%H_%M")
            cv2.imwrite(f'{PATH}/{now_class}/{now_class}_{dt_string}_{count}', frame)
            time.sleep(1)
            if cv2.waitKey(1) & 0xff == ord(' '):
                cv2.destroyAllWindows()
                break




