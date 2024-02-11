import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def test_new(self):
        """Test if new method adds object to __objects."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, storage.all())

    def test_save_reload(self):
        """Test if save and reload methods serialize and deserialize correctly."""
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = User()
        obj3 = User()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.save()
        storage = FileStorage()
        storage.reload()
        self.assertIn(obj1.__class__.__name__ + '.' + obj1.id, storage.all())
        self.assertIn(obj2.__class__.__name__ + '.' + obj2.id, storage.all())
        self.assertIn(obj3.__class__.__name__ + '.' + obj3.id, storage.all())

    def test_serialize_deserialize(self):
        """Test if _serialize_obj and _deserialize_obj methods work correctly."""
        storage = FileStorage()
        obj = User()
        serialized_obj = storage._serialize_obj(obj)
        deserialized_obj = storage._deserialize_obj(serialized_obj)
        self.assertIsInstance(deserialized_obj, User)
        self.assertEqual(obj.id, deserialized_obj.id)
        self.assertEqual(obj.created_at, deserialized_obj.created_at)
        self.assertEqual(obj.updated_at, deserialized_obj.updated_at)

if __name__ == '__main__':
    unittest.main()

