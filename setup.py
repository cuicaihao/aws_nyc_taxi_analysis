from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='New York City Taxi and Limousine Commission (TLC) Trip Record Data Demo. ABC company is a ride hailing company, they have large volume of subscribe users using their mobile app to get transportation services from local drivers. The mobile app for passengers and drivers will upload activities data to server for data analyst. ABC company wants to leverage AI/Machine Learning technologies to improve their business. One of their key requirements is demand forecast. They prefer to split a city into different grid, and forecast the demand in each grid at 5min, 15min and 30min slot. If the demand goes high in future, ABC company will increase the price in that grid to slow down the demands.',
    author='Chris Cui',
    license='MIT',
)
