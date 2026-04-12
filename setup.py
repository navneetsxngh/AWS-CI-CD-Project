from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
# Read requirements.txt 
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads requirements.txt and returns a clean list of packages.
    It removes '-e .' which is only needed for local editable installs.
    """
    requirements = []

    with open(file_path, "r", encoding="utf-8") as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ML-project_Learning",
    version="0.0.1",
    author="Navneet Singh",
    author_email="singhnavneet2587@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt"),
    description="End-to-End ML Project for learning deployment and pipelines",
    python_requires=">=3.8",
)