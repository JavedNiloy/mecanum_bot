from setuptools import setup

package_name = 'mecanum_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/mecanum_bot_launch.py', 'launch/view_bot_launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/mecanum_bot.urdf']),
        ('share/' + package_name + '/rviz', ['rviz/mecanum_bot.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='soap',
    maintainer_email='tasnimjaved.niloy@gmail.com',
    description='ROS2 package for Mecanum robot simulation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mecanum_controller = mecanum_bot.mecanum_controller:main',
        ],
    },
)
