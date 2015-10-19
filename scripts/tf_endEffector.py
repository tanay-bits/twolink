#!/usr/bin/env python 

import rospy
# import math
import tf
from visualization_msgs.msg import Marker

if __name__ == '__main__':
    rospy.init_node('tf_endEffector_node')

    listener = tf.TransformListener()

    pubber = rospy.Publisher('visualization_marker', Marker, queue_size=10)

    rate = rospy.Rate(15.0)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('endEffector', 'base', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        marker = Marker()
        marker.header.frame_id = "endEffector"
        marker.header.stamp = rospy.Time(0)
        marker.id = 0
        marker.type = 2
        marker.action = 0
        marker.pose.position.x = trans[0]
        marker.pose.position.y = trans[1]
        marker.pose.position.z = trans[2]
        marker.pose.orientation.x = rot[0]
        marker.pose.orientation.y = rot[1]
        marker.pose.orientation.z = rot[2]
        marker.pose.orientation.w = rot[3]
        marker.scale.x = 0.1
        marker.scale.y = 0.1
        marker.scale.z = 0.1
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0


        pubber.publish(marker)

        rate.sleep()


