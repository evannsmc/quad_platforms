from setuptools import setup, find_packages

package_name = 'quad_platforms'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='egmc',
    maintainer_email='egmc@todo.todo',
    description='Shared platform configurations for quadrotor control',
    license='MIT',
)
