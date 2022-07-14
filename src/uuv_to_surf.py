#! /usr/bin/python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry

rospy.init_node('uuv_to_surf')
pub = rospy.Publisher('/uuv_surf_uncert', PoseWithCovarianceStamped, queue_size=10)

def uuv_pose_callback(msg):
    pwcs = PoseWithCovarianceStamped()
    pwcs.header.stamp = rospy.get_rostime()
    pwcs.header.frame_id = 'world'
    pwcs.pose.pose.orientation.x = 0
    pwcs.pose.pose.orientation.y = 0
    pwcs.pose.pose.orientation.z = 0
    pwcs.pose.pose.orientation.w = 1

    pwcs.pose.pose.position.x = msg.pose.pose.position.x
    pwcs.pose.pose.position.y = msg.pose.pose.position.x
    pwcs.pose.pose.position.z = 0.1
    pwcs.pose.covariance = [0 for _ in range(6 ** 2)]
    pwcs.pose.covariance[0] = 1
    pwcs.pose.covariance[7] = 1
    pwcs.pose.covariance[14] = 1

rospy.Subscriber('/ar_tag_pos', Odometry, uuv_pose_callback) 



rospy.spin()
