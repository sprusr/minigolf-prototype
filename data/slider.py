import serial
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time


class Slider():
    def __init__(self, serial_device='/dev/tty.usbserial'):
        self.ser = serial.Serial(serial_device, 9600)
        mh = Adafruit_MotorHAT(addr=0x60)
        self.motor = mh.getMotor(3)
        #self.motor_setup()

    """
    def motor_setup(self):
        self.motor.run(Adafruit_MotorHAT.FORWARD)
        self.motor.setSpeed(255)
        time.sleep(0.5)
        self.motor.setSpeed(0)
        time.sleep(0.5)
        self.maxpos = ser.readline()
        self.motor.run(Adafruit_MotorHAT.BACKWARD)
        self.motor.setSpeed(255)
        time.sleep(0.5)
        self.motor.setSpeed(0)
        time.sleep(0.5)
        self.minpos = ser.readline()
    """

    def get_pos(self):
        return int(self.ser.readline()[:-1])

    def is_touched(self):
        return self.ser.readline()[1:] == 1

    def set_pos(self, pos, speed=100):
        while (self.get_pos != pos):
            if self.get_pos > pos:
                self.motor.run(Adafruit_MotorHAT.FORWARD)
                self.motor.setSpeed(speed)
            else:
                self.motor.run(Adafruit_MotorHAT.BACKWARD)
                self.motor.setSpeed(speed)
