# Author(s): 'Neelesh Batham' <neelesh.batham007@gmail.com

import os
from setuptools import setup, find_packages

current_dir = os.path.dirname(os.path.realpath(__file__))
direc = os.path.dirname(os.path.realpath(__file__))


def parse_requirements():
    packages_array = []
    requirements_file = open(direc + os.sep + 'requirements.txt')
    for line in requirements_file:
        if line.strip() == '#Testing':
            break
        if line.strip():
            packages_array.append(line)
    return packages_array

setup(
    name='jsonxml',
    version="v1",
    include_package_data=True,
    install_requires=parse_requirements(),
    packages=find_packages(exclude=[
        'tests',
        'tests.*',
        '*.tests',
        '*.tests.*',
    ]),
    # For installing dependencies using Ansible.
    data_files=[('./', ['requirements.txt'])],
    url='https://github.com/neeleshbatham/',
    license='Neelesh Batham',
    author='Neelesh Batham',
    author_email='neelesh.batham007@gmail.com',
    description='JSON to XML'
)
