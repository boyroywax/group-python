from credentials import Credentials
from data import Data
from nonce import Nonce
from owner import Owner
from verified_object import VerifiedObject
from universal_object import UniversalObject

class Verification():
    """
    A class that verifies Universal Objects,
    and returns Verified Objects
    """

    def __init__(self):
        """
        Initializes the object
        """
        pass

    def verify(self, universal_object: UniversalObject) -> VerifiedObject:
        """
        Verifies a universal object
        """
        if not isinstance(universal_object, UniversalObject):
            raise TypeError("universal_object must be a UniversalObject")

        return VerifiedObject(
            universal_object.name,
            universal_object.description,
            Nonce(universal_object.nonce),
            Owner(universal_object.owner),
            Credentials(universal_object.creds),
            Data(universal_object.data)
        )
    
    def verify_all(self, universal_objects: list) -> list:
        """
        Verifies a list of universal objects
        """
        if not isinstance(universal_objects, list):
            raise TypeError("universal_objects must be a list")
        if not all(isinstance(obj, UniversalObject) for obj in universal_objects):
            raise TypeError("universal_objects must be a list of UniversalObjects")

        return [self.verify(obj) for obj in universal_objects]
