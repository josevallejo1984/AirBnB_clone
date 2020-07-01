#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import os
import sys
from models.base_model import BaseModel
from time import sleep
from models import storage
import models
import pep8 as pycodestyle
from unittest import mock
module_doc = models.base_model.__doc__


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""
    def class_none(self):
        my_model = BaseModel(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_input(self):
        """checks for valid input """
        my_model = BaseModel()
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertIsNotNone(BaseModel)
        self.assertIn(BaseModel(), storage.all().values())
        my_model.name = "Holberton"
        my_model.my_number = 89.533535
        self.assertTrue(89.533535 == my_model.my_number and
                        my_model.name == "Holberton")
        self.assertIsInstance(my_model, BaseModel)


class TestBaseModel_json(unittest.TestCase):
    """Unittests for testing json."""
    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_init(self):
        """test init"""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_my_model_json(self):
        """Test my model json"""
        my_model = BaseModel()
        my_model_2 = BaseModel()
        my_model.name = "Carlos"
        my_model.dict_name = {'Name_1': 'Carlos', 'Age_1': 24,
                              'Name_2': 'Jose', 'Age_2': 32}
        my_model.empty_name = ""
        my_model.empty_list_name = []
        my_model.list_name = ["Carlos", "Barros"]
        my_model.my_number = 27
        my_model.none_name = None
        my_model.my_number_inf = float('inf')
        my_model.my_number_nan = float('nan')
        my_model_json = my_model.to_dict()
        self.assertNotEqual(type(my_model_json), type(my_model))
        self.assertNotEqual(my_model.id, my_model_2.id)
        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")

        for key, value in my_model_json.items():
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
        my_model = BaseModel()
        sleep(0.05)
        my_model_2 = BaseModel()
        self.assertLess(my_model.created_at, my_model_2.created_at)
        self.assertLess(my_model.updated_at, my_model_2.updated_at)

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

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_save_reload_base_model(self):
        """Test save reload base model"""
        all_objs = storage.all()
        self.assertTrue((type(all_objs) == dict) and
                        (not isinstance(type(all_objs), BaseModel)))

        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(type(obj_id) == str)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
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
