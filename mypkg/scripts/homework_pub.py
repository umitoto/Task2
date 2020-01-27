#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('homework_pub')
    pub = rospy.Publisher('mes', String, queue_size=50)
    #rate = rospy.Rate(10)
    while not rospy.is_shutdown(): #終了処理がされるまで無限ループ
        mes = String()
        input_key = None
        print "comand ->"
        input_key = raw_input()
        
        #mes.data = "ros homework"
        pub.publish(input_key)
        #rate.sleep()
