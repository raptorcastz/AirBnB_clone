#!/usr/bin/python3
"""Test for the console"""
import unittest
import console
from console import HBNBCommand
class test_console(unittest.TestCase):
    """class test console"""

    def create(self):
        """create the intance"""
        return HBNBCommand()

    def test_quit(self):
        """ test for the method quit
        """
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """test for the method EQF
        """
       console = self.create()
        self.assertTrue(console.onecmd("EOF"))