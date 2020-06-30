#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import json
import sys
from models.base_model import BaseModel
from models import storage


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def test_input(self):
        """checks for valid input """
        my_model = BaseModel()
        self.assertIsNotNone(BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89.533535
        self.assertTrue(89.533535 == my_model.my_number and my_model.name == "Holberton")
        self.assertIsInstance(my_model, BaseModel)

    def test_my_model_json(self):
        """Test my model json"""
        my_model = BaseModel()
        my_model.name = "Carlos"
        my_model.dict_name = {'Name_1': 'Carlos', 'Age_1': 24, 'Name_2': 'Jose', 'Age_2': 32}
        my_model.empty_name = ""
        my_model.empty_list_name = []
        my_model.list_name = ["Carlos", "Barros"]
        my_model.my_number = 27
        my_model.none_name = None
        my_model.my_number_inf = float('inf')
        my_model.my_number_nan = float('nan')

        my_model_json = my_model.to_dict()
        self.assertNotEqual(type(my_model_json), type(my_model))

        for key, value in my_model_json.items():
            if key == "__class__":
                self.assertIs(value, my_model.__class__.__name__)
            elif key == "updated_at":
                self.assertIn(value, my_model.updated_at.isoformat())
            elif key == "created_at":
                self.assertIn(value, my_model.created_at.isoformat())
            else:
                self.assertIn(value, my_model.__dict__.values())

    def test_base_model_dict(self):
        """Test base model dict"""
        my_model = BaseModel()
        my_model.name = "Betty"
        my_model.my_number = 12.89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(isinstance(my_new_model, BaseModel))
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

    def test_save_reload_base_model(self):
        """Test save reload base model"""
        all_objs = storage.all()
        self.assertTrue((type(all_objs) == dict) and (not isinstance(type(all_objs), BaseModel)))

        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(type(obj_id) == str)


if __name__ == "__main__":
    unittest.main()
