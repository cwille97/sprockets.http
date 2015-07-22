#!/usr/bin/env python
#

import os.path
import sys

import setuptools

from sprockets import http


def read_requirements(filename):
    requirements = []
    try:
        with open(os.path.join('requires', filename)) as req_file:
            for line in req_file:
                if '#' in line:
                    line = line[:line.index('#')]
                line = line.strip()
                if line.startswith('-r'):
                    line = line[2:].strip()
                    requirements.extend(read_requirements(filename))
                else:
                    requirements.append(line)
    except IOError:
        pass
    return requirements


requirements = read_requirements('installation')
tests_require = read_requirements('testing')

setuptools.setup(
    name='sprockets.http',
    version=http.__version__,
    description='Tornado HTTP application runner',
    author='AWeber Communications',
    url='https://github.com/sprockets/sprockets.http',
    install_requires=requirements,
    license='BSD',
    namespace_packages=['sprockets'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Tornado',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='nose.collector',
    tests_require=tests_require,
    zip_safe=True,
)
