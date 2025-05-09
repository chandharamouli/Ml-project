from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith('#')
        ]

setup(
    name='your_project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
)

