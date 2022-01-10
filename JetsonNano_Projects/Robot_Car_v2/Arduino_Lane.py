from SerialModule import ConnectArd
from LaneDetectionModule import getLaneCurve
import WebcamModule


###################################################
SENSITIVITY = 1.3
MAX_VAL = 0.3
WEIGHT = 100
###################################################


def main():
    connector = ConnectArd()
    ser = connector.initConnection('/dev/ttyACM0', 9600)

    while True:
        img = WebcamModule.getImg()
        curveVal, img = getLaneCurve(img, 1, normalization=False)
        sen = SENSITIVITY
        if curveVal > MAX_VAL * WEIGHT:
            curveVal = MAX_VAL * WEIGHT
        elif curveVal < -MAX_VAL * WEIGHT:
            curveVal = -MAX_VAL * WEIGHT

        if curveVal > 0:
            sen = SENSITIVITY + 0.4
            if curveVal < 0.05 * WEIGHT:
                curveVal = 0
        else:
            if curveVal > -0.08 * WEIGHT:
                curveVal = 0

        connector.sendData(ser, curveVal * sen, 4)




