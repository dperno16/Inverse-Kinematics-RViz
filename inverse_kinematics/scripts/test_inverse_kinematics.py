#!/usr/bin/env python3
import rospy
import numpy as np
from math import pi
from std_msgs.msg import Header
from sensor_msgs.msg import JointState
from inverse_kinematics import inverse_kinematics

class Manipulator():
	def __init__(self):
		rospy.init_node('manipulator')
		rospy.loginfo("Press Ctrl + C to terminate")
		self.rate = rospy.Rate(1000)
		self.joint_pub = rospy.Publisher('/rx150/joint_states', JointState, queue_size=10)
		
		# prepare joint message to publish
		joint_msg = JointState()
		joint_msg.header = Header()
		joint_msg.name = ['waist', 'shoulder', 'elbow', 'wrist_angle','wrist_rotate', 'gripper', 'left_finger', 'right_finger']
		joint_msg.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.026, -0.026]
		
		# test case for inverse kinematics (position [x, y, z] in meter)
		case1 = [0.200, 0.000, 0.254]
		case2 = [0.17320, 0.10000, 0.25391]
		case3 = [0.02165, 0.01250, 0.29721]
		case4 = [-0.012, 0.038, 0.261]
		
		# adjust the test case here
		test_case = case4
		joint_angle = inverse_kinematics(test_case)
		np.set_printoptions(suppress=True)
		print("joint angles (deg) = ", np.around(np.rad2deg(joint_angle), 3))
		print("target position (m) = ", np.around(test_case, 3))
		while not rospy.is_shutdown():
			joint_msg.header.stamp = rospy.Time.now()
			joint_msg.position[0:3] = joint_angle
			self.joint_pub.publish(joint_msg)
			self.rate.sleep()
		
if __name__ == '__main__':
	whatever = Manipulator()