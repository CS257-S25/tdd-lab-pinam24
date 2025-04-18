'''
A file for tests for the production code.
'''

from io import StringIO
import unittest
from unittest.main import main
from production import reverse_word
import sys

class TestReverseWord(unittest.TestCase):
    '''
    A class to test the reverse_word function.
    '''
    def test_reverse_word(self):
        '''
        Test the reverse_word function.
        '''
        self.assertEqual(reverse_word('hello'), 'olleh')
        self.assertEqual(reverse_word('world'), 'dlrow')
        self.assertEqual(reverse_word(''), '')
        self.assertEqual(reverse_word('a'), 'a')
        self.assertEqual(reverse_word('ab'), 'ba')
        
class TestCommandLine(unittest.TestCase):
    def test_command_line_output(self):
        # Simulate command-line arguments
        sys.argv = ['production.py', 'this is a test']

        # Redirect stdout so we can capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the main function (which should read from sys.argv and print result)
        main()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Get printed result and test it
        printed_output = captured_output.getvalue().strip()
        self.assertEqual(printed_output, 'siht si a tset')  # expected output