import json
from typing import Dict, List, Optional

from credentials import Credentials
from data import Data
from nonce import Nonce
from owner import Owner
from universal_object import UniversalObject


class VerifiedObject():
    """
    A class that represents a verified object
    """
    def __init__(
        self,
        name: str,
        description: str,
        nonce: Nonce,
        owner: Owner,
        creds: Credentials,
        data: Data

    ):
        """
        Initializes the object
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(description, str):
            raise TypeError("description must be a string")

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
            'nonce': self.nonce.__json__(),
            'owner': self.owner.__json__(),
            'creds': self.creds.__json__(),
            'data': self.data.__json__()
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
