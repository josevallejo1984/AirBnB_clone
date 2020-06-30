#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import os
import sys
from models.state import State
from time import sleep
from models import storage
import models
module_doc = models.state.__doc__


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""
    def class_none(self):
        my_model = State(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def class_none(self):
        my_model = State(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_input(self):
        """checks for valid input """
        my_model = State()
        self.assertEqual(State, type(State()))
        self.assertIsNotNone(State)
        self.assertIn(State(), storage.all().values())
        my_model.id = "asdfa8sdf5asdf5as1d"
        my_model.name = "Carlos"
        self.assertTrue("Carlos" == my_model.name and
                        my_model.id == "asdfa8sdf5asdf5as1d")
        self.assertIsInstance(my_model, State)


class TestState_json(unittest.TestCase):
    """Unittests for testing json."""

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_my_model_json(self):
        """Test my model json"""
        my_model = State()
        my_model_2 = State()
        my_model.name = "Carlos"
        my_model.user_id = {'Name_1': 'Carlos', 'Age_1': 24,
                            'Name_2': 'Jose', 'Age_2': 32}
        my_model.city_id = ""
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
        my_model = State()
        sleep(0.05)
        my_model_2 = State()
        self.assertLess(my_model.created_at, my_model_2.created_at)
        self.assertLess(my_model.updated_at, my_model_2.updated_at)

    def test_State_dict(self):
        """Test base model dict"""
        my_model = State()
        my_model.name = "Betty"
        my_model.longitude = 28.51
        my_model_json = my_model.to_dict()
        my_new_model = State(**my_model_json)
        self.assertTrue(isinstance(my_new_model, State))
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


class TestState_save(unittest.TestCase):
    """Unittests for testing save method of the State class."""

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

    def test_save_reload_State(self):
        """Test save reload base model"""
        all_objs = storage.all()
        self.assertTrue((type(all_objs) == dict) and
                        (not isinstance(type(all_objs), State)))

        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(type(obj_id) == str)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_updates_file(self):
        state = State()
        state.save()
        stateid = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(stateid, f.read())


if __name__ == "__main__":
    unittest.main()
