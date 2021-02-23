#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sensor_msgs.msg
import random
import numpy as np
from geometry_msgs.msg import Twist
from itertools import *
from operator import itemgetter

linear_speed = 0.0 #Always forward linear velocity.
thresh_distance = 1.5 #THRESHOLD value for laser scan.
PI = 3.1415
Kp = 0.05
angular_speed = 0

def LaserScanProcess(data):
    range_angels = np.arange(len(data.ranges))
    ranges = np.array(data.ranges)
    range_mask = (ranges > thresh_distance)
    ranges = list(range_angels[range_mask])
    max_gap = 40
    # print(ranges)
    gap_list = []
    for k, g in groupby(enumerate(ranges), lambda (i,x):i-x):
        gap_list.append(map(itemgetter(1), g))
    gap_list.sort(key=len)
    largest_gap = gap_list[-1]
    min_angle, max_angle = largest_gap[0]*((data.angle_increment)*180/PI), largest_gap[-1]*((data.angle_increment)*180/PI)
    average_gap = (max_angle - min_angle)/2

    turn_angle = min_angle + average_gap

    print(min_angle, max_angle)
    print(max_gap,average_gap,turn_angle)

    global linear_speed
    global angular_speed
    if average_gap < max_gap:
        angular_speed = -0.5
    else:
        linear_speed = 0.3
        angular_speed = Kp*(-1)*(90 - turn_angle)

def main():
    rospy.init_node('listener', anonymous=True)

    pub = rospy.Publisher('husky_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("kernel/scan", sensor_msgs.msg.LaserScan , LaserScanProcess)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        command = Twist()
        command.linear.x = linear_speed
        command.angular.z = angular_speed
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    main()