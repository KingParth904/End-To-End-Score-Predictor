from setuptools import find_packages, setup
from typing import List

HYPH_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters and any extra spaces
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present
        if HYPH_E_DOT in requirements:
            requirements.remove(HYPH_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Parth',
    author_email='anshusadotra0148@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Fixed the typo
)
