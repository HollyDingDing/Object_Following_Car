import serial
import time


class ConnectArd:
    def initConnection(self, portNo, baudRate):
        try:
            ser = serial.Serial(portNo, baudRate)
            print("Device Connected")
            return ser
        except:
            print("Not Connected")


    def sendData(self, se, data, digits):
        myString = "$"
        for d in data:
            myString += str(d).zfill(digits)
        try:
            se.write(myString.encode())
            print(myString)
        except:
            print("Data transmission Failed")


if __name__ == "__main__":
    connector = ConnectArd()
    ser = connector.initConnection("/dev/ttyACM0", 9600)
    while True:
        connector.sendData(ser, [0, 255], 3)
        time.sleep(1)
        connector.sendData(ser, [0, 0], 3)
        time.sleep(1)




