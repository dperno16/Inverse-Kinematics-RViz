#!/usr/bin/env python3
import numpy as np
import rospy
from math import pi, cos, sin, atan2, acos, sqrt

def inverse_kinematics(position):
	# input: the position of end effector [x, y, z]
	# output: joint angles [joint1, joint2, joint3]
	x = position[0]
	y = position[1]
	z = position[2]
	
	# add your code here to complete the computation and calculate joint 1,joint 2 and joint 3 values

	a=0.1581 #distance from joint 1 to joint 2, same a for both alpha and beta triangleslaw of cosines
	b1=0.150 #alpha triangle vertical distance from joint 2 to 3
	c1=0.050 #horizontal distance form joint 2 to 3
	c2=0.150 # link 4 length
	d1=0.1039 #link 1 length
	
	r = sqrt(np.square(x)+np.square(y)) #distance from origin to the posiiton of the end effector
	s = z - d1
	b2=sqrt(np.square(r) + np.square(s)) #distance from joint 2 to the end effector
	gamma = atan2(s,r)
	beta1=acos((np.square(a)+np.square(b2)-np.square(c2))/(2*a*b2))
	beta2=acos((np.square(a)+np.square(c2)-np.square(b2))/(2*a*c2))
	alpha = atan2(c1,b1) #spong 5.22
	psi=(pi/2)-alpha
	phi=pi-psi

	joint1 = atan2(y,x) #spong 5.20
	joint2 = (pi/2)-alpha-beta1-gamma
	joint3 = beta2-phi
	
	print("r: " , r)
	print("s: " , s)
	print("phi: ", phi)
	print("alpha: ", alpha)
	print("psi: ", psi)
	print("x: " , x)
	print("y: " , y)
	print("z: " , z)
	print("joint1: " , joint1)
	print("joint2: " , joint2)
	print("joint3: " , joint3)
	
	return [joint1, joint2, joint3]