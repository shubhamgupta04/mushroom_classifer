from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "mushroom-classifer"
VERSION = "0.0.2"
AUTHOR = "Shubham Gupta"
DESCRIPTION = "This is a Machine Learning Project"

REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages(),
install_requires = get_requirements_list()


)
