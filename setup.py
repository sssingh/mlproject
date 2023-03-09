from setuptools import setup, find_packages
from typing import List


def get_dependencies(req_file_path: str) -> List[str]:
    """
    This function will return a list of required packages
    """
    with open(req_file_path) as fp:
        requirements = fp.readlines()
        requirements = [
            pkg.replace("\n", "") for pkg in requirements if "-e" not in pkg
        ]
        return requirements


setup(
    name="mlprojects",
    version="1.0.0",
    author="Sunil S. Singh",
    author_email="sunil.singh@datamatrix.com",
    url="https://github.com/sssingh/mlproject",
    packages=find_packages(),
    install_requires=get_dependencies("requirements.txt"),
)
