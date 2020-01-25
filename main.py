#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

# Initialize a motor (by default this means clockwise, without any gears).
MotorOne = Motor(Port.A)
MotorTwo = Motor(Port.D)
SensorOne = ColorSensor(Port.S2)
Left = MotorOne
Right  = MotorTwo
robot = DriveBase(Left, Right, 56, 84) #UNITS MM!
touchSensor1 = TouchSensor(Port.S3)

driveForward = -200 ## turn up speeds for day of!
turnSpeed = 80
brick.sound.file('swvader02.wav')
brick.sound.file('swvader02.wav')

while True:
    robot.drive(driveForward, 0)
    print("Driving")
    print(SensorOne.reflection()) ## Having issues with ambient
    #Others have been recommending reflection 
    #rather than ambient, larger range to work with/threshold, more reliable?
    if SensorOne.reflection() < 1:
        robot.stop(Stop.BRAKE)
        wait(5)
        robot.drive(-driveForward, 0)
        wait(1000)
        print("Reversing 1")
        wait(5)
        i = 0
        while i < 25:
            robot.drive(-driveForward, turnSpeed)
            wait(5)
            print("Turning")
            if SensorOne.reflection() < 1:
                robot.stop(Stop.BRAKE)
                robot.drive(-driveForward, 0)
                print("reversing 2")
            i = i + 1
    if touchSensor1 == True:
        robot.drive(driveForward * 5, 0)
        wait(6000)


    
