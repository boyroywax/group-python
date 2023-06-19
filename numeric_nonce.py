from typing import List, Optional

from nonce import Nonce
from universal_object import UniversalObject


class NumericNonce:
    """
    A class for managing numeric nonces
    """
    def __init__(self, obj: Optional[UniversalObject] = None, nonce: Optional[List] = None):
        """
        Initializes a numeric nonce
        """
        if obj is not None:
            if not isinstance(obj.nonce, list):
                raise ValueError('Invalid nonce')
            nonce = obj.nonce
        if nonce is None:
            raise ValueError('Nonce cannot be None')
        if not isinstance(nonce, list) or not nonce:
            raise ValueError('Invalid nonce')
        self.nonce: Nonce = Nonce(nonce)
        self.pre = self.nonce.pre
        self.active: int = self.nonce.active

        if not isinstance(self.active, int):
            raise TypeError('Active nonce is not an integer')

        self.next: int = self.active + 1

    def is_valid_type(self) -> bool:
        """
        Checks if the active nonce is an integer
        """
        return isinstance(self.active, int)

    def get_next(self) -> int:
        """
        Returns the next nonce
        """
        return self.next

    def increment(self) -> None:
        """
        Increments a nonce
        """
        if not self.is_valid_type():
            raise TypeError('Active nonce is not an integer')
        self.active = self.next
        self.next = self.active + 1

    def __str__(self) -> str:
        """
        Returns the string representation of the active nonce
        """
        return str(self.active)

    def __repr__(self) -> str:
        """
        Returns the string representation of the active nonce
        """
        return str(self.active)

    def __json__(self) -> dict:
        """
        Returns the JSON representation of the nonce
        """
        return {'pre': self.pre, 'active': self.active, 'next': self.next}