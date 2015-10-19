#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from math import sin, cos, acos, atan2, pi, sqrt

def desired_thetas(t, T):
    xd = 0.5*cos(2*pi*t/T) + 1.25
    yd = 0.5*sin(2*pi*t/T)
    r = sqrt(xd**2 + yd**2)

    alpha = acos(1 - (r**2)/2)
    beta = acos(r/2)

    theta2 = pi - alpha
    theta1 = atan2(yd, xd) - beta

    return [theta1, theta2]



def sender():
    jspub = rospy.Publisher('joint_states', JointState, queue_size=10)

    rospy.init_node('controller_node')
    R = rospy.get_param('~controller_pub_rate')
    rate = rospy.Rate(R)

    T = rospy.get_param('~period')

    cmd = JointState()

    while not rospy.is_shutdown():
        cmd.header.stamp = rospy.Time.now()
        t = rospy.get_time()

        cmd.name = ['baseHinge', 'interArm']
        cmd.position = desired_thetas(t, T)

        jspub.publish(cmd)

        rate.sleep()



if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass

