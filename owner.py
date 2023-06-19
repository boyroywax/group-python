from typing import List


class Owner():
    """
    A class for managing owners
    """
    def __init__(self, owner: List):
        self._owner = owner

    def show(self):
        print(self._owner)

    def __str__(self):
        return str(self._owner)

    def __json__(self):
        return str(self._owner)
