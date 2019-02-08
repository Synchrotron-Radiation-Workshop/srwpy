import os
import sys
from subprocess import run as sub_run
from distutils.command.build import build
from setuptools import setup, find_packages, Extension

# NOTE: This file must remain Python 2 compatible for the foreseeable future,
# to ensure that we error out properly for people with outdated setuptools
# and/or pip.
min_version = (2, 7)
if sys.version_info < min_version:
    error = '''
srwpy does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
'''.format(*(list(sys.version_info[:2]) + list(min_version)))
    sys.exit(error)

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

# Prepare the extension:
srwlpy_kwargs = {'include_dirs': ['core/src/lib'],
                 'libraries': ['srw', 'fftw'],
                 'sources': ['core/src/clients/python/srwlpy.cpp']}

if sys.platform == 'win32':
    srwlpy_kwargs['library_dirs'] = ['core/vc']
    srwlpy_kwargs['extra_compile_args'] = ['/MT']
else:
    srwlpy_kwargs['library_dirs'] = ['core/gcc']

srwlpy = Extension('srwlpy', **srwlpy_kwargs)

class VinylSRWBuild(build):
    '''
    This class is a wrapper around the classic build to run the makefile on srw
    before to create librairies
    '''
    def run(self):
        sub_run(['make', '-C', os.path.join(here, 'core'), 'all'])
        super().run()
        sub_run(['make', '-C', os.path.join(here, 'core'), 'clean'])

setup(
    name='vinyl_srw',
    version='1.0.0',
    cmdclass={'build': VinylSRWBuild},
    description='Synchrotron Radiation Workshop',
    long_description=readme,
    author='NSLS-II, Brookhaven National Lab',
    author_email='mrakitin@bnl.gov',
    url='https://github.com/PaNOSC-ViNYL/srwpy',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    license='BSD (3-clause)',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    ext_modules=[srwlpy],
)
