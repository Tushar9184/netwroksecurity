from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    This function will return the requirments
    """
    requriemnts_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file_obj:
            lines = file_obj.readlines()
            for line in lines:
                requriemnts=line.strip()
                if requriemnts and requriemnts!='-e .':
                    requriemnts_list.append(requriemnts)
            return requriemnts_list
    except FileNotFoundError:
        print("file not found error")


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Tushar",
    author_email="sabharwaltushar02@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)