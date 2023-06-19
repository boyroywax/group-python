from typing import Dict


class Data():
    """
    A class that manages the data of a verified object
    """

    def __init__(self, data: Dict) -> None:
        """
        Initializes the data
        """
        if not isinstance(data, dict):
            raise ValueError('Invalid data')
        self._data = data

    @property
    def data(self) -> Dict:
        """
        Returns the data
        """
        return self._data

    @data.setter
    def data(self, data: Dict) -> None:
        """
        Sets the data
        """
        self._data = data

    @data.deleter
    def data(self) -> None:
        """
        Deletes the data
        """
        self._data = None

    @data.getter
    def data(self) -> Dict:
        """
        Returns the data
        """
        return self._data

    def __json__(self) -> Dict:
        """
        Returns the data
        """
        return self.data

    def __str__(self) -> str:
        """
        Returns the data as a string
        """
        return str(self.data)

    def __repr__(self) -> str:
        """
        Returns the data as a string
        """
        return str(self.data)

    def __eq__(self, other) -> bool:
        """
        Returns True if the data is equal to the other data
        """
        return self.data == other.data

    def __ne__(self, other) -> bool:
        """
        Returns True if the data is not equal to the other data
        """
        return self.data != other.data
