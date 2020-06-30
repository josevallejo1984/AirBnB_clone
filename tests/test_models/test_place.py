#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import os
import sys
from models.place import Place
from time import sleep
from models import storage
from unittest import mock
import models
module_doc = models.place.__doc__


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""
    def class_none(self):
        my_model = Place(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def class_none(self):
        my_model = Place(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_input(self):
        """checks for valid input """
        my_model = Place()
        self.assertEqual(Place, type(Place()))
        self.assertIsNotNone(Place)
        self.assertIn(Place(), storage.all().values())
        my_model.id = "asdfa8sdf5asdf5as1d"
        my_model.name = "Carlos"
        self.assertTrue("Carlos" == my_model.name and
                        my_model.id == "asdfa8sdf5asdf5as1d")
        self.assertIsInstance(my_model, Place)


class TestPlace_json(unittest.TestCase):
    """Unittests for testing json."""

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_my_model_json(self):
        """Test my model json"""
        my_model = Place()
        my_model_2 = Place()
        my_model.name = "Carlos"
        my_model.user_id = {'Name_1': 'Carlos', 'Age_1': 24,
                            'Name_2': 'Jose', 'Age_2': 32}
        my_model.Place_id = ""
        my_model.number_bathrooms = [3, 2, 5]
        my_model.amenity_ids = ["Carlos", "Barros"]
        my_model.price_by_night = 25.25
        my_model.name = None
        my_model.latitude = float('inf')
        my_model.longitude = float('nan')

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
        my_model = Place()
        sleep(0.05)
        my_model_2 = Place()
        self.assertLess(my_model.created_at, my_model_2.created_at)
        self.assertLess(my_model.updated_at, my_model_2.updated_at)

    def test_Place_dict(self):
        """Test base model dict"""
        my_model = Place()
        my_model.name = "Betty"
        my_model.longitude = 28.51
        my_model_json = my_model.to_dict()
        my_new_model = Place(**my_model_json)
        self.assertTrue(isinstance(my_new_model, Place))
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


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

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

    def test_save_reload_Place(self):
        """Test save reload base model"""
        all_objs = storage.all()
        self.assertTrue((type(all_objs) == dict) and
                        (not isinstance(type(all_objs), Place)))

        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(type(obj_id) == str)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_save_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_updates_file(self):
        place = Place()
        place.save()
        placeid = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(placeid, f.read())

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = Place()
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
