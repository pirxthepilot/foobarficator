from setuptools import find_packages
from setuptools import setup

from foobarficator import __version__


setup(
    name='foobarficator',
    version=__version__,
    author='Mawhrin-Skel',
    description='Foobarficate all the things',
    url='https://github.com/pirxthepilot/foobarficator',
    license='MIT',
    packages=find_packages(exclude=('tests',)),

    install_requires=[
        'requests~=2.23.0',
    ],

    entry_points={
        'console_scripts': [
            'foo = foobarficator.foo:main',
            'bar = foobarficator.bar:main',
        ]
    }
)
