"""Installs QuickWeb using distutils

Run:
    python setup.py install

to install this package.
"""

from setuptools import setup

name = "SDL2pymunk"
version = "0.0.1"

desc = "pymunk's 2D physics simulation, integrated with PySDL2's sprites"
long_desc = "Library that provides pymunk's based 2D simulation, integrated with PySDL2's sprites"

classifiers = '''
Development Status :: 1 - Planning
Intended Audience :: Developers
License :: Freely Distributable
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.5
Topic :: Internet :: WWW/HTTP :: WSGI
Topic :: Internet :: WWW/HTTP :: WSGI :: Application
Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware
Topic :: Internet :: WWW/HTTP :: WSGI :: Server
'''

requirements = '''
PySDL2
pymunk
'''

setup(
    name=name,
    version=version,
    description=desc,
    long_description=long_desc,
    author='SDL2pymunk Developers',
    author_email='lamego.pinto@gmail.com',
    classifiers=[x for x in classifiers.splitlines() if x],
    install_requires=[x for x in requirements.splitlines() if x],
    url='http://www.mywayos.org/',
    packages=[
        "sdl2pymunk",
    ],
    include_package_data=True,
    package_data={'examples': ['*.py']},
)
