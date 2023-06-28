from setuptools import find_packages,setup
from typing import List

Constan = '-e .'

def get_requirements(file_path:str) -> List[str]:
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n","") for req in requirments]
        
        if Constan in requirments:
            requirments.remove(Constan)

        return requirments


setup(
    name = 'DiamondPricePrediction',
    version = '0.0.1',
    author = 'koushik',
    author_email = 'saikoushik.gsk@gmail.com',
    install_requires = get_requirements('requirments.txt'),
    packages = find_packages()
)