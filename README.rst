Movie Recommender-cli
=====================

*A movie recommender command line program in Python.*


Purpose
-------

This is a movie recommender application that was developed in order to give the opportunity for anyone to be able to recommend movies in an easy and simple way.

The idea of this project is: create a command line python application that
takes as input a number of movie ID's and this data file. The application
should then calculate and output, a list of movie recommendations, based on
the list and the data file.


Usage
-----

If you're in the project folder, and want to install the library, the command
you'll want to run is::

    $ pip install .[movie-recommender]

If you want to run all tests for this project, you would run the following
command::

    $ python setup.py test

This will trigger `py.test <http://pytest.org/latest/>`_, along with its popular
`coverage <https://pypi.python.org/pypi/pytest-cov>`_ plugin.

To execute the application, you should run the following command::

    $ movirecommender <number_movies> <file_path>

Extra
-----
This project depends of the **docopt**, a Python Package that helps to create
beautiful command-line interfaces.
To install this Python package, we can execute the following command::

    $ pip install docopt

