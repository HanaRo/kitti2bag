#!/usr/bin/env python

from setuptools import setup

setup(
    name='kitti2bag',
    version='1.6',
    description='Convert KITTI dataset to ROS bag file the easy way!',
    author='Tomas Krejci',
    author_email='tomas@krej.ci',
    maintainer='Haoran Zhou',
    maintainer_email='hanaro.chou@gmail.com',
    url='https://github.com/HanaRo/kitti2bag',
    keywords = ['dataset', 'ros', 'rosbag', 'kitti'],
    entry_points = {
        'console_scripts': ['kitti2bag=kitti2bag.__main__:main'],
    },
    install_requires=['pykitti', 'progressbar2']
)
