#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()
        user = User()
        self.assertIn("State." + state.id, self.storage.all())
        self.assertIn("City." + city.id, self.storage.all())
        self.assertIn("Amenity." + amenity.id, self.storage.all())
        self.assertIn("Place." + place.id, self.storage.all())
        self.assertIn("Review." + review.id, self.storage.all())
        self.assertIn("User." + user.id, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods"""
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()
        user = User()
        state_id = "State." + state.id
        city_id = "City." + city.id
        amenity_id = "Amenity." + amenity.id
        place_id = "Place." + place.id
        review_id = "Review." + review.id
        user_id = "User." + user.id
        self.storage.save()
        models.storage.reload()
        self.assertIn(state_id, self.storage.all())
        self.assertIn(city_id, self.storage.all())
        self.assertIn(amenity_id, self.storage.all())
        self.assertIn(place_id, self.storage.all())
        self.assertIn(review_id, self.storage.all())
        self.assertIn(user_id, self.storage.all())

    def test_reload(self):
        """Test reload method"""
        self.storage.save()
        state = State()
        self.storage.reload()
        self.assertIn("State." + state.id, self.storage.all())


if __name__ == "__main__":
    unittest.main()
