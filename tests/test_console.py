#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the test"""
        storage.reset()

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            user_id = output.split()[3][1:-1]
            user_instance = storage.all()["User.{}".format(user_id)]
            self.assertIsInstance(user_instance, User)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            user_id = output.split()[3][1:-1]
            self.console.onecmd(f"show User {user_id}")
            self.assertIn(user_id, f.getvalue())

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            user_id = output.split()[3][1:-1]
            self.console.onecmd(f"destroy User {user_id}")
            self.assertNotIn(user_id, storage.all())

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn("[User]", output)
            self.assertEqual(output.count("[User]"), 2)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            user_id = output.split()[3][1:-1]
            self.console.onecmd(f"update User {user_id} first_name John")
            user_instance = storage.all()[f"User.{user_id}"]
            user_dict = user_instance.to_dict()
            self.assertIn("John", user_dict.values())

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("count User")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")

    def test_invalid_command(self):
        """Test invalid command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("invalid_command")
            output = f.getvalue().strip()
            self.assertEqual(output, "*** Unknown syntax: invalid_command")


if __name__ == "__main__":
    unittest.main()
