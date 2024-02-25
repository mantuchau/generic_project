from setuptools import find_packages,setup



setup(
name='mlproject',
version='0.0.1',
author='mantu',
author_email='kumar290081998@gmail.com',
packages=find_packages(),
install_requires=get_requirements('reqirements.txt')

)