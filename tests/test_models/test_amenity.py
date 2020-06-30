#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import os
import sys
from models.amenity import Amenity
from time import sleep
from models import storage
from unittest import mock
import models
module_doc = models.amenity.__doc__


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""
    def class_none(self):
        my_model = Amenity(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def class_none(self):
        my_model = Amenity(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_input(self):
        """checks for valid input """
        my_model = Amenity()
        self.assertEqual(Amenity, type(Amenity()))
        self.assertIsNotNone(Amenity)
        self.assertIn(Amenity(), storage.all().values())
        my_model.email = "carlos@holberton.com"
        my_model.first_name = "Carlos"
        self.assertTrue("Carlos" == my_model.first_name and
                        my_model.email == "carlos@holberton.com")
        self.assertIsInstance(my_model, Amenity)


class TestAmenity_json(unittest.TestCase):
    """Unittests for testing json."""

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_my_model_json(self):
        """Test my model json"""
        my_model = Amenity()
        my_model_2 = Amenity()
        my_model.first_name = "Carlos"
        my_model.dict_name = {'Name_1': 'Carlos', 'Age_1': 24,
                              'Name_2': 'Jose', 'Age_2': 32}
        my_model.password = ""
        my_model.first_name = []
        my_model.last_name = ["Carlos", "Barros"]
        my_model.password = "27"
        my_model.name = None
        my_model.password = float('inf')
        my_model.password = float('nan')

        my_model_json = my_model.to_dict()
        self.assertNotEqual(type(my_model_json), type(my_model))
        self.assertNotEqual(my_model.id, my_model_2.id)

        for key, value in my_model_json.items():
            self.assertTrue(type(key) == str)
            if key == "__class__":
                self.assertIs(value, my_model.__class__.__name__)
            elif key == "updated_at":
                self.assertIn(value, my_model.updated_at.isoformat())
            elif key == "created_at":
                self.assertIn(value, my_model.created_at.isoformat())
            else:
                self.assertIn(value, my_model.__dict__.values())

    def test_two_models_different_created_at(self):
        """Test differents created_at"""
        my_model = Amenity()
        sleep(0.05)
        my_model_2 = Amenity()
        self.assertLess(my_model.created_at, my_model_2.created_at)
        self.assertLess(my_model.updated_at, my_model_2.updated_at)

    def test_Amenity_dict(self):
        """Test base model dict"""
        my_model = Amenity()
        my_model.first_name = "Betty"
        my_model.password = "12.89"
        my_model_json = my_model.to_dict()
        my_new_model = Amenity(**my_model_json)
        self.assertTrue(isinstance(my_new_model, Amenity))
        self.assertNotEqual(my_new_model, my_model)
        self.assertTrue(my_new_model.__dict__ == my_model.__dict__)

        for key, value in my_new_model.__dict__.items():
            if key == "__class__":
                self.assertIs(value, my_model.__class__.__name__)
            elif key == "updated_at":
                self.assertEqual(value, my_model.updated_at)
            elif key == "created_at":
                self.assertEqual(value, my_model.created_at)
            else:
                self.assertTrue(value, my_model.__dict__.values())


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_reload_Amenity(self):
        """Test save reload base model"""
        all_objs = storage.all()
        self.assertTrue((type(all_objs) == dict) and
                        (not isinstance(type(all_objs), Amenity)))

        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(type(obj_id) == str)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_save_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save_updates_file(self):
        amenity = Amenity()
        amenity.save()
        amenityid = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(amenityid, f.read())

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = Amenity()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new())
        self.assertTrue(mock_storage.save())


if __name__ == "__main__":
    unittest.main()
