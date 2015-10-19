#!/usr/bin/env python 

import rospy
# import math
import tf
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

if __name__ == '__main__':
    rospy.init_node('tf_endEffector_node')

    listener = tf.TransformListener()

    pubber = rospy.Publisher('visualization_marker', Marker, queue_size=10)
    
    R = rospy.get_param('~tf_ee_pub_rate')
    rate = rospy.Rate(R)
    while not rospy.is_shutdown():
        try:
            (trans, rot) = listener.lookupTransform('base', 'endEffector', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        # points = Marker()
        line_strip = Marker()

        # points.header.frame_id = "base"
        line_strip.header.frame_id = "base"
        
        # points.header.stamp = rospy.Time(0)
        line_strip.header.stamp = rospy.Time(0)
        
        # points.ns = "points_and_lines"
        # line_strip.ns = "points_and_lines"

        # points.action = 0
        line_strip.action = 0

        # points.pose.orientation.x = rot[0]
        # points.pose.orientation.y = rot[1]
        # points.pose.orientation.z = rot[2]
        # points.pose.orientation.w = 1.0
        # line_strip.pose.orientation.x = rot[0]
        # line_strip.pose.orientation.y = rot[1]
        # line_strip.pose.orientation.z = rot[2]
        line_strip.pose.orientation.w = 1.0

        # points.id = 0
        line_strip.id = 0

        # points.type = 8
        line_strip.type = 4

        # points.scale.x = 0.1
        # points.scale.y = 0.1

        line_strip.scale.x = 0.2

        # points.color.a = 1.0
        # points.color.r = 0.0
        # points.color.g = 1.0
        # points.color.b = 0.0

        line_strip.color.a = 1.0
        line_strip.color.r = 0.0
        line_strip.color.g = 0.0
        line_strip.color.b = 1.0

        p = Point()
        p.x = trans[0]
        p.y = trans[1]
        p.z = trans[2]

        # points.points.append(p)
        line_strip.points.append(p)
        

        # pubber.publish(points)
        pubber.publish(line_strip)

        rate.sleep()


