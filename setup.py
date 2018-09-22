from setuptools import setup, find_packages
import re

with open('requirements.txt', 'r') as requirements_file:
    REQUIRED_PACKAGES = requirements_file.read()

regex = r"(\d*\.\d*)"
with open('__version__.py') as version_file:
    VERSION = re.findall(regex, version_file.read())[0]

setup(name='cheat',
      version=VERSION,
      description='An awesome cheatsheet manager',
      url='https://github.com/MCSH/cheat',
      author='Sajjad Heydari',
      author_email='mcshemail@gmail.com',
      license='MIT',
      install_requires=REQUIRED_PACKAGES,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False, package_data={'cheats': ['*.yaml'], },
entry_points={'console_scripts': ['cheat = cheat:main'], })
