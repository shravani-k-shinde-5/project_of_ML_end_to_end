from setuptools import find_packages,setup
def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.readlines()
    requirements = [req.replace("\n","") for req in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

setup(
  name ="mlproject",
  version="0.0.1",
  author ="shravani",
  author_email="shravanishinde857@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)