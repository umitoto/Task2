#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

def mes_function(message):
    if(message.data == '1'):
        GPIO.output(14, True)
    elif(message.data == '0'):
        GPIO.output(14, False)
    

if __name__=='__main__':
    rospy.init_node('homework_sub')
    sub = rospy.Subscriber('mes', String, mes_function)
    rospy.spin() 
    GPIO.cleanup()
