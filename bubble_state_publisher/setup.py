'''
Author: Ligcox
Date: 2022-07-11 18:16:41
FilePath: /bubble_bringup/home/nvidia/Desktop/bubble/src/bubble_navigation/bubble_state_publisher/setup.py
LastEditors: Ligcox
LastEditTime: 2022-07-13 13:15:20
License: GNU General Public License v3.0. See LICENSE file in root directory.
Copyright (c) 2022 Birdiebot R&D Department
Shanghai University Of Engineering Science. All Rights Reserved
'''
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages
package_name = 'bubble_state_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('description/*')),
        (os.path.join('share', package_name), glob('mashes/*')),
        (os.path.join('share', package_name), glob('rviz/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nvidia',
    maintainer_email='zyhbum@foxmail.com',

    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'state_publisher = bubble_state_publisher.statePublisher:main'
        ],
    },
)
