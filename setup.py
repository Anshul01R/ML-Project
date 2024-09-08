from  setuptools import find_packages, setup
from typing import List

HYPEN_e = '-e .'

def get_requirements(file_path : str)-> List[str]:
    """_summary_
    
    This function will return list of requirements

    Args:
        file_path (str): file path where the requirement are stored
    Returns:
        List[str]: List of library that have to be installed while installing setup 
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPEN_e in requirements:
        requirements.remove(HYPEN_e)
        
    return requirements

setup(
    name = 'My ML_Project',
    version = '0.0.1',
    author = 'Anshul Singh',
    author_email= 'singhans031@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')    
)