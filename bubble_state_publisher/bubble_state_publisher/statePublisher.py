'''
Author: Ligcox
Date: 2022-07-11 22:42:20
FilePath: /bubble/build/bubble_state_publisher/bubble_state_publisher/chassis.py
LastEditors: Ligcox
LastEditTime: 2022-07-12 23:50:37
License: GNU General Public License v3.0. See LICENSE file in root directory.
Copyright (c) 2022 Birdiebot R&D Department
Shanghai University Of Engineering Science. All Rights Reserved
'''

from math import *
import rclpy
from rmctrl_msgs.msg import Gimbal
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Quaternion
from rclpy.node import Node

def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)


class StatePublisher(Node):
    def __init__(self) -> None:
        super().__init__("StatePublisher")

        self.gimbal_sub = self.create_subscription(
            Gimbal, "/status/gimbal", self.gimbal_callback, 1)

        self.joint_pub = self.create_publisher(JointState, 'joint_states', 10)

    def gimbalinfo_callback(self, data:Gimbal):
        pass

    def gimbal_callback(self, data:Gimbal):
        now = self.get_clock().now()

        joint_state = JointState()
        joint_state.header.stamp = now.to_msg()
        joint_state.name = ["yaw_joint", "pitch_joint"]
        joint_state.position = [data.yaw, data.pitch]
        self.joint_pub.publish(joint_state)


def main(args=None):
    rclpy.init(args=args)
    state_publisher = StatePublisher()
    rclpy.spin(state_publisher)
    state_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
