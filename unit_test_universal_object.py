import unittest

from nonce import Nonce
from numeric_nonce import NumericNonce
from universal_object import UniversalObject


class TestNonce(unittest.TestCase):
    def setUp(self):
        self.nonce = Nonce()

    def test_nonce_property(self):
        self.assertIsNone(self.nonce.nonce)
        self.nonce.nonce = [1, 2, 3]
        self.assertEqual(self.nonce.nonce, [1, 2, 3])
        del self.nonce.nonce
        self.assertIsNone(self.nonce.nonce)

    def test_get_active(self):
        self.assertIsNone(self.nonce.active)
        self.nonce.nonce = [1, 2, 3]
        self.assertEqual(self.nonce.active, 3)
        self.nonce.nonce = ["1", "2", "3"]
        self.assertEqual(self.nonce.active, "3")

    def test_delete_nonce(self):
        self.assertIsNone(self.nonce.nonce)
        self.nonce.nonce = [1, 2, 3]
        self.assertEqual(self.nonce.nonce, [1, 2, 3])
        del self.nonce.nonce
        self.assertIsNone(self.nonce.nonce)


class TestNumericNonce(unittest.TestCase):
    def setUp(self):
        self.nonce = NumericNonce(nonce=[1, 2, 3])

    def test_nonce_property(self):
        self.assertEqual(self.nonce.active, 3)
        self.nonce.active = 4
        self.assertEqual(self.nonce.active, 4)

    def test_get_next(self):
        self.assertEqual(self.nonce.get_next(), 4)

    def test_increment(self):
        self.assertEqual(self.nonce.active, 3)
        self.nonce.increment()
        self.assertEqual(self.nonce.active, 4)

    def test_is_valid_type(self):
        self.assertTrue(self.nonce.is_valid_type())
        self.nonce.active = "3"
        self.assertFalse(self.nonce.is_valid_type())

    def test_json(self):
        self.assertEqual(
            self.nonce.__json__(),
            {'pre': [1, 2], 'active': 3, 'next': 4}
        )

    def test_invalid_nonce(self):
        with self.assertRaises(ValueError):
            NumericNonce(nonce=None)
        with self.assertRaises(ValueError):
            NumericNonce(nonce=[])
        with self.assertRaises(TypeError):
            NumericNonce(nonce=[1, 2, "3"])

    def test_invalid_active_nonce(self):
        with self.assertRaises(TypeError):
            NumericNonce(nonce=[1, 2, "3"])

    def test_set_active_nonce(self):
        self.nonce.active = 4
        self.assertEqual(self.nonce.active, 4)

    def test_increment_non_integer(self):
        self.nonce.active = "3"
        with self.assertRaises(TypeError):
            self.nonce.increment()

    def test_get_next_after_increment(self):
        self.nonce.increment()
        self.assertEqual(self.nonce.get_next(), 5)


class TestUniversalObject(unittest.TestCase):
    def setUp(self):
        self.test_schema: str = """{
                        \"type\": \"object\",
                        \"properties\": {
                            \"name\": {
                                \"type\": \"string\"
                            },
                            \"age\": {
                                \"type\": \"integer\"
                            }
                        }
                    }"""
        self.obj = UniversalObject(**{
                "name": "My Object",
                "description": "This is my object.",
                "nonce": [1, 2, 3],
                "owner": ["John Doe"],
                "creds": ["admin", "user"],
                "data": {"title": "My Object", "schema": self.test_schema}
            }
        )

    def test_name_property(self):
        self.assertEqual(self.obj.name, "My Object")

    def test_description_property(self):
        self.assertEqual(self.obj.description, "This is my object.")

    def test_nonce_property(self):
        self.assertEqual(self.obj.nonce, [1, 2, 3])

    def test_owner_property(self):
        self.assertEqual(self.obj.owner, "John Doe")

    def test_creds_property(self):
        self.assertEqual(self.obj.creds, ["admin", "user"])

    def test_data_property(self):
        self.assertEqual(
            self.obj.data,
            {"title": "My Object", "schema": self.test_schema}
        )

    def test_str_data_property(self):
        self.assertIsInstance(
            UniversalObject(
                **{
                    "name": "My Object",
                    "description": "This is my object.",
                    "nonce": [1, 2, 3],
                    "owner": ["John Doe"],
                    "creds": ["admin", "user"],
                    "data": "invalid json"
                }
            ).get_data(),
            str
        )

    def test_get_data_dict(self):
        self.assertIsInstance(
            self.obj.get_data_dict(),
            dict
        )

    def test_get_data_type(self):
        self.assertEqual(
            self.obj.get_data_type(),
            dict
        )

    def test_dict_data_property(self):
        self.assertIsInstance(
            UniversalObject(
                **{
                    "name": "My Object",
                    "description": "This is my object.",
                    "nonce": [1, 2, 3],
                    "owner": ["John Doe"],
                    "creds": ["admin", "user"],
                    "data": {"title": "My Object", "schema": self.test_schema}
                }
            ).get_data(),
            dict
        )

    def test_json(self):
        self.assertEqual(
            self.obj.__json__(),
            {
                "name": "My Object",
                "description": "This is my object.",
                "nonce": [1, 2, 3],
                "owner": ["John Doe"],
                "creds": ["admin", "user"],
                "data": {"title": "My Object", "schema": self.test_schema}
            }
        )


if __name__ == '__main__':
    unittest.main()
