import os
from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', pip.download.PipSession())

# reqs is a list of requirement
reqs = [str(ir.req) for ir in install_reqs]

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pykss-styleguide',
    version='0.0.1',
    packages=['django-pykss-styleguide'],
    install_requires=reqs,
    include_package_data=True,
    description='The django-pykss-styleguide',
    long_description=README,
    url='https://github.com/annikaC/django-pykss-styleguide',
    author='Annika Clarke',
    author_email='annika.clarke@gmail.com',
)
