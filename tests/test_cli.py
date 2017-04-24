#
# Author: Jeferson Moura
# Germany - 7nd February
#
from subprocess import PIPE, Popen as popen
from unittest import TestCase
from movierecommender import __version__ as VERSION


class TestCli(TestCase):
    """Class with tests for cli"""

    def test_help(self):
        """Test if it is returning the help information"""
        helpinfo = popen(['movierecommender', '-h'], stdout=PIPE).\
            communicate()[0]

        self.assertIn('Usage:', helpinfo)
        self.assertIn('Options:', helpinfo)
        self.assertIn('Arguments:', helpinfo)
        self.assertIn('Example:', helpinfo)
        self.assertIn('Help:', helpinfo)

    def test_version(self):
        """Test if it is returning the help information"""
        version = popen(['movierecommender', '--version'], stdout=PIPE).\
            communicate()[0]
        self.assertEqual(version.strip(), VERSION)

    def test_zero_argument(self):
        """Test no arguments"""
        info = popen(['movierecommender', ''], stdout=PIPE).\
            communicate()[0]
        self.assertNotIn('Options:', info)

    def test_one_argument(self):
        """Test only one argument"""
        info = popen(['movierecommender', '2'], stdout=PIPE). \
            communicate()[0]
        self.assertNotIn('Options:', info)

    def test_no_int_number_movies(self):
        """Test giving no integer as number_movies"""
        info = popen(['movierecommender', 'nonumber'], stdout=PIPE). \
            communicate()[0]
        self.assertNotIn('Options:', info)

    def test_no_file(self):
        """Test giving a address without json file"""
        info = popen(['movierecommender', '2'], stdout=PIPE). \
            communicate()[0]
        self.assertNotIn('Options:', info)
