import os
import sys

from codecs import open

from setuptools import setup, find_packages


VERSION = '0.1'


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

    
requires = ['requests']


with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='pyBuildWeb',
    version=VERSION,
    description='BuildWeb helper service.',
    long_description=readme,
    author='Rocky Ramchandani',
    author_email='riverdale1109@gmail.com',
    url='https://github.com/rocky1109/pyBuildWeb',
    keywords='vmware devops buildweb',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
)
