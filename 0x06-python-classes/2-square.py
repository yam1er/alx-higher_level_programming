#!/usr/bin/python3
"""Size validation"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """new square

        Args:
            size (int): The size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
