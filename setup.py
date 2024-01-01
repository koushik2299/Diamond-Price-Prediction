from setuptools import find_packages,setup 
from typing import List

def get_requirment(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
    name = 'DiamonPricePrediction',
    author = 'Koushik',
    version = '0.0.1',
    author_email="saikoushik.gsk@gmail.com",
    install_requires = get_requirment('requirments.txt'),
    packages = find_packages()
)