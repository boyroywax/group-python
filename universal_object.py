import json
from typing import Dict, List, Optional

class UniversalObject():
    """
    A class that represents a universal object
    """
    def __init__(
        self,
        name: str,
        description: str,
        nonce: List,
        owner: List,
        creds: List,
        data: Dict or List or str or int or float or bool

    ):
        """
        Initializes the object
        """
        self.name = name
        self.description = description
        self.nonce = nonce
        self.owner = owner
        self.creds = creds
        self.data = data

    def __json__(self) -> dict:
        """
        Returns a JSON representation of the object
        """
        return {
            'name': self.name,
            'description': self.description,
            'nonce': self.nonce,
            'owner': self.owner,
            'creds': self.creds,
            'data': self.data
        }

    def __str__(self) -> str:
        """
        Returns a string representation of the object
        """
        return str(self.__json__())

    def __repr__(self) -> str:
        """
        Returns a string representation of the object
        """
        return str(self.__json__())

    def __eq__(self, other) -> bool:
        """
        Returns true if the objects are equal
        """
        return self.__json__() == other.__json__()

    def __ne__(self, other) -> bool:
        """
        Returns true if the objects are not equal
        """
        return self.__json__() != other.__json__()

    def __hash__(self) -> int:
        """
        Returns the hash of the object
        """
        return hash(str(self.__json__()))

    def __getitem__(self, key) -> str:
        """
        Returns the value of the key
        """
        return self.__json__()[key]

    def __setitem__(self, key, value) -> None:
        """
        Sets the value of the key
        """
        self.__json__()[key] = value

    def __delitem__(self, key) -> None:
        """
        Deletes the key
        """
        del self.__json__()[key]

    def __contains__(self, key) -> bool:
        """
        Returns true if the key is in the object
        """
        return key in self.__json__()

    def contains_data(self) -> bool:
        """
        Checks if the object contains data
        """
        return self.data is not None

    def get_data_type(self) -> Optional[Dict or List or str or int or bool]:
        """
        Returns the object's data type
        """
        return type(self.data)

    def get_data(self) -> Optional[Dict or List or str or int or bool]:
        """
        Returns the object's data
        """
        return self.data

    def get_data_dict(self) -> Optional[Dict]:
        """
        Returns the object's data as a dictionary
        """
        if not isinstance(self.data, dict):
            return json.loads(self.data)
        return self.data

    def get_data_value(self, key) -> str:
        """
        Gets a value from the object's data
        """
        return self.data[key]

    def safe_get_data_value(self, key) -> str:
        """
        Safely gets a value from the object's data
        """
        if key in self.data:
            return self.data[key]
        else:
            return None

    def set_data(self, data) -> None:
        """
        Sets the object's data, overwriting the previous data
        """
        self.data = data

    def safe_set_data_value(self, key, value) -> None:
        """
        Safely sets a value in the object's data
        """
        if key in self.data:
            self.data[key] = value
        else:
            return None

    def set_data_value(self, key, value) -> None:
        """
        Sets a value in the object's data
        """
        self.data[key] = value

    def data_contains_schema(self) -> bool:
        """
        Checks if the object's data has a schema
        """
        return self.data['schema'] is not None

    def get_schema(self) -> dict:
        """
        Returns the object's schema
        """
        return json.loads(self.data['schema'])

    def safe_get_schema_value(self, key) -> str:
        """
        Safely gets a value from the object's schema
        """
        if key in self.get_schema():
            return self.get_schema()[key]
        else:
            return None

    def get_schema_value(self, key) -> str:
        """
        Gets a value from the object's schema
        """
        return self.get_schema()[key]

    def safe_set_schema_value(self, key, value) -> None:
        """
        Safely sets a value in the object's schema
        """
        if key in self.get_schema():
            self.get_schema()[key] = value
        else:
            return None

    def set_schema_value(self, key, value) -> None:
        """
        Sets a value in the object's schema
        """
        self.get_schema()[key] = value

    def check_for_population(self) -> bool:
        """
        Verifies that the object is populated
        """
        try:
            assert self.name is not None
            assert self.description is not None
            assert self.nonce is not None
            assert self.owner is not None
            assert self.creds is not None
            assert self.data is not None
        except (AssertionError):
            return False
        return True
