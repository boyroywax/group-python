from typing import Dict, List, Optional


class Nonce:
    """
    A class for managing nonces
    """
    def __init__(self, nonce: Optional[List] = None):
        """
        Initializes a nonce
        """
        if nonce is not None:
            if not isinstance(nonce, list):
                raise ValueError('Invalid nonce')
            self._nonce = nonce
        else:
            self._nonce: Optional[List] = None

    @property
    def nonce(self) -> Optional[List]:
        """
        Returns the nonce
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: List) -> None:
        """
        Sets the nonce
        """
        self._nonce = nonce

    @nonce.deleter
    def nonce(self) -> None:
        """
        Deletes the nonce
        """
        self._nonce = None

    @nonce.getter
    def nonce(self) -> Optional[List]:
        """
        Returns the nonce
        """
        return self._nonce

    @property
    def active(self) -> Optional[str or int or float or bool or Dict or List]:
        """
        Returns the active nonce
        """
        return self.nonce[-1] if self.nonce is not None else None

    @active.getter
    def active(self) -> Optional[str or int or float or bool or Dict or List]:
        """
        Returns the active nonce
        """
        return self.nonce[-1] if self.nonce is not None else None

    @active.setter
    def active(self, value: str or int or float or bool or Dict or List) -> None:
        """
        Sets the active nonce
        """
        self.nonce[-1] = value

    @active.deleter
    def active(self) -> None:
        """
        Deletes the active nonce
        """
        self.nonce[-1] = None

    @property
    def pre(self) -> Optional[str or int or float or bool or Dict or List]:
        """
        Returns the pre nonce
        """
        return self.nonce[:-1] if self.nonce is not None else None

    @pre.getter
    def pre(self) -> Optional[str or int or float or bool or Dict or List]:
        """
        Returns the pre nonce
        """
        return self.nonce[:-1] if self.nonce is not None else None

    @pre.setter
    def pre(self, value: str or int or float or bool or Dict or List) -> None:
        """
        Sets the pre nonce
        """
        self.nonce[:-1] = value

    @pre.deleter
    def pre(self) -> None:
        """
        Deletes the pre nonce
        """
        self.nonce[:-1] = None

    def __str__(self) -> str:
        """
        Returns the string representation of the nonce
        """
        return str(self.nonce)
    
    def __repr__(self) -> str:
        """
        Returns the string representation of the nonce
        """
        return str(self.nonce)
    
    def __json__(self) -> Dict:
        """
        Returns the JSON representation of the nonce
        """
        return self.nonce
    
