from typing import List, Optional, Dict

class Credentials():
    """
    A class for managing credentials
    """

    def __init__(self, creds: List):
        """
        Initializes credentials
        """
        if isinstance(creds, list):
            self._creds = creds
        else:
            raise TypeError('Invalid credentials, not a list')
    
    @property
    def creds(self) -> Optional[List]:
        """
        Returns the credentials
        """
        return self._creds
    
    @creds.setter
    def creds(self, creds: List) -> None:
        """
        Sets the credentials
        """
        self._creds = creds

    @creds.deleter
    def creds(self) -> None:
        """
        Deletes the credentials
        """
        self._creds = None

    @creds.getter
    def creds(self) -> Optional[Dict]:
        """
        Returns the credentials
        """
        return self._creds

    def __json__(self) -> Optional[List]:
        """
        Returns the credentials
        """
        creds = {}
        i: int = 0
        for cred in self.creds:
            creds[i] = self.creds[i]
            i += 1

        return creds
    
    def __str__(self) -> str:
        """
        Returns the credentials as a string
        """
        creds = {}
        i: int = 0
        for cred in self.creds:
            creds[i] = self.creds[i]
            i += 1
        return creds.__str__()
    
    def __repr__(self) -> str:
        """
        Returns the credentials as a string
        """
        creds = {}
        i: int = 0
        for cred in self.creds:
            creds[i] = self.creds[i]
            i += 1
        return creds.__str__()
    