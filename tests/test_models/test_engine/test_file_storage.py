#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime

class TestFileStorage(unittest.TestCase):
    """Test cases for file storage"""

    def setUp(self):
        """Set up for the test"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method"""
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertIs(obj_dict, self.storage._FileStorage__objects)

    def test_new(self):
        """Test new method"""
        state = State()
        self.assertIn("State." + state.id, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods"""
        state = State()
        city = City()
        state_id = "State." + state.id
        city_id = "City." + city.id
        self.storage.save()
        models.storage.reload()
        self.assertIn(state_id, self.storage.all())
        self.assertIn(city_id, self.storage.all())

    def test_reload(self):
        """Test reload method"""
        self.storage.save()
        state = State()
        self.storage.reload()
        self.assertIn("State." + state.id, self.storage.all())

if __name__ == "__main__":
    unittest.main()

