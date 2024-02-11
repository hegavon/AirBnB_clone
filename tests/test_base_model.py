#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel class"""

    def setUp(self):
        """Set up for the test"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down the test"""
        del self.base_model

    def test_instance(self):
        """Test instance creation"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id(self):
        """Test id attribute"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertRegex(self.base_model.id,
                         '^[0-9a-f]{8}-[0-9a-f]{4}-'
                         '[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        """Test save method"""
        self.base_model.save()
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(base_model_dict['created_at'], str)
        self.assertIsInstance(base_model_dict['updated_at'], str)

    def test_str(self):
        """Test __str__ method"""
        string = str(self.base_model)
        self.assertIsInstance(string, str)
        self.assertIn('[BaseModel]', string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)


if __name__ == "__main__":
    unittest.main()
