import unittest

from credentials import Credentials
from data import Data
from nonce import Nonce
from owner import Owner
from verification import Verification
from verified_object import VerifiedObject
from universal_object import UniversalObject


class TestVerifiedObject(unittest.TestCase):
    def setUp(self):
        self.nonce = Nonce([0, 1])
        self.creds = Credentials(["vc1", "vc2"])
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
        self.data = Data({
            "title": "My Object",
            "schema": self.test_schema
        })
        self.owner = Owner("John Doe")
        self.obj = VerifiedObject(
                    "Test_Object",
                    "This is a test object",
                    self.nonce,
                    Owner("John Doe"),
                    self.creds,
                    self.data
        )

        self.expected = VerifiedObject(**{
            'name': 'Test_Object',
            'description': 'This is a test object',
            'nonce': self.nonce,
            'owner': Owner('John Doe'),
            'creds': self.creds,
            'data': self.data
        })

    def test_equality(self):
        self.assertEqual(self.obj, self.expected)

    def test_json(self):
        self.assertEqual(self.obj.__json__(), self.expected.__json__())

    def test_str(self):
        self.assertEqual(self.obj.__str__(), self.expected.__str__())

    def test_repr(self):
        self.assertEqual(self.obj.__repr__(), self.expected.__repr__())

    def test_eq(self):
        obj2 = VerifiedObject("Test_Object", "This is a test object", self.nonce, "John Doe", self.creds, self.data)
        self.assertEqual(self.obj, obj2)
        assert self.obj.__eq__(obj2) is True

    def test_ne(self):
        obj2 = VerifiedObject("Test_Object 2", "This is another test object", self.nonce, "Jane Doe", self.creds, self.data)
        self.assertNotEqual(self.obj, obj2)

    def test_invalid_name(self):
        with self.assertRaises(TypeError):
            VerifiedObject(
                123,
                "This is a test object",
                self.nonce,
                Owner("John Doe"),
                self.creds,
                self.data
            )

    def test_invalid_description(self):
        with self.assertRaises(TypeError):
            VerifiedObject(
                "Test_Object",
                123,
                self.nonce,
                Owner("John Doe"),
                self.creds,
                self.data
            )

    def test_invalid_nonce(self):
        with self.assertRaises(ValueError):
            VerifiedObject(
                "Test_Object",
                "This is a test object",
                Nonce("invalid_nonce"),
                Owner("John Doe"),
                self.creds,
                self.data
            )

    def test_invalid_owner(self):
        with self.assertRaises(TypeError):
            VerifiedObject(
                "Test_Object",
                "This is a test object",
                self.nonce,
                Owner(),
                self.creds,
                self.data
            )

    def test_invalid_creds(self):
        with self.assertRaises(TypeError):
            VerifiedObject(
                "Test_Object",
                "This is a test object",
                self.nonce,
                Owner("John Doe"),
                Credentials("invalid_creds"),
                self.data
            )

    def test_invalid_data(self):
        with self.assertRaises(ValueError):
            VerifiedObject(
                "Test_Object",
                "This is a test object",
                self.nonce,
                Owner("John Doe"),
                self.creds,
                Data("invalid_data")
            )

    def test_invalid_verification(self):
        universal_obj = UniversalObject(
            name="Test_Object",
            description="This is a test object",
            nonce=1234,
            owner=["John Doe"],
            creds=["vc1", "vc2"],
            data={
                "title": "My Object",
                "schema": self.test_schema
            }
        )
        with self.assertRaises(ValueError):
            Verification().verify(universal_obj)


if __name__ == '__main__':
    unittest.main()
