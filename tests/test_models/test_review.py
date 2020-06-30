#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import os
import sys
from models.review import Review
from time import sleep
from models import storage
import models
module_doc = models.review.__doc__


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""
    def class_none(self):
        my_model = Review(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def class_none(self):
        my_model = Review(None)
        self.assertNotIn(None, my_model.__dict__.values())

    def test_input(self):
        """checks for valid input """
        my_model = Review()
        self.assertEqual(Review, type(Review()))
        self.assertIsNotNone(Review)
        self.assertIn(Review(), storage.all().values())
        my_model.user_id = "asdfa8sdf5asdf5as1d"
        my_model.Review_id = "Carlos"
        self.assertTrue("Carlos" == my_model.Review_id and
                        my_model.user_id == "asdfa8sdf5asdf5as1d")
        self.assertIsInstance(my_model, Review)


class TestReview_json(unittest.TestCase):
    """Unittests for testing json."""

    def setUp(self):
        """set up"""
        pass

    def tearDown(self):
        """tearDown"""
        pass

    def test_my_model_json(self):
        """Test my model json"""
        my_model = Review()
        my_model_2 = Review()
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
        my_model = Review()
        sleep(0.05)
        my_model_2 = Review()
        self.assertLess(my_model.created_at, my_model_2.created_at)
        self.assertLess(my_model.updated_at, my_model_2.updated_at)

    def test_Review_dict(self):
        """Test base model dict"""
        my_model = Review()
        my_model.name = "Betty"
        my_model.longitude = 28.51
        my_model_json = my_model.to_dict()
        my_new_model = Review(**my_model_json)
        self.assertTrue(isinstance(my_new_model, Review))
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


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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

    def test_save_reload_Review(self):
        """Test save reload base model"""
        all_objs = storage.all()
        self.assertTrue((type(all_objs) == dict) and
                        (not isinstance(type(all_objs), Review)))

        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(type(obj_id) == str)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_save_with_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        review = Review()
        review.save()
        reviewid = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(reviewid, f.read())


if __name__ == "__main__":
    unittest.main()
