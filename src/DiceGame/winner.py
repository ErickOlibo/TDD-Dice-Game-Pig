"""This module manages the characteristics of the winner object."""
import time


class Winner:
    """Serve as a data structure to save game's winner stats."""

    def __init__(self, name: str, score: int, stamp=round(time.time())):
        self._stamp = stamp
        self._name = name
        self._score = score
        self._data = [self._stamp, self._name, self._score]

    @property
    def data(self) -> list:
        """

        Function: Get the data stored in the instance.

        Description:
            This property returns the value of the `_data` attribute of the current
            instance, which is a list of data that has been collected or generated
            by the instance. The `@property` decorator allows you to access this
            attribute as if it were a regular property of the object, without
            needing to call a separate method. This is useful for providing a more
            natural interface to the data, and for encapsulating the internal
            workings of the object.

        Returns:
            list: The data stored in the instance.
        """
        return self._data

    @property
    def name(self) -> str:
        """
        Function: Returns the name of the object.

        Return : A string representing the name of the object.
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Function: Sets the name of the object.

        Args:
         - name: A string representing the new name of the object.

        """
        self._name = name

    @property
    def to_string(self) -> str:
        """

        Function: Returns a string representation of the object.

        Return: A string representing the object's properties.

        """
        return f'{self._stamp} | {self._name} - {self._score}'

    def get_name(self) -> str:
        """
        Function: Returns the name of the object.

        Return : A string representing the name of the object.
        """
        return self._name
