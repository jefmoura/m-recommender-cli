#
# Author: Jeferson Moura
# Germany - 4nd February
#
from codecs import open
from os.path import abspath, dirname, join
from subprocess import call
from setuptools import Command, find_packages, setup
from movierecommender import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=movierecommender',
                      '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'movie-recommender',
    version = __version__,
    description = 'A movie recommender command line program in Python.',
    author = 'Jeferson Moura',
    author_email = 'jefmmoreira@gmail.com',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'movierecommender=movierecommender.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
