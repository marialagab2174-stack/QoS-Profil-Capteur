from setuptools import find_packages, setup

package_name = 'tp_qos_robotique'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lagab-maria',
    maintainer_email='marialagab2174@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
entry_points={
        'console_scripts': [
            'lidar_sub = tp_qos_robotique.lidar_subscriber:main',
            'cmd_pub = tp_qos_robotique.command_publisher:main',
        ],
    },
)
