# it is used to make our machine learning model as package so we can use it as per our requirement
from  setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return list of requirements
    '''

    requirements = []
    with open('requirements.txt') as f:
        requirements = f.readlines()
        requirements = [i.replace("\n","") for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    

    return requirements





# it is basically metadata of this project
setup(

    name="mlproject",
    version="0.0.1",
    author="Aditya",
    author_email="aditya.gaikwad415@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)
