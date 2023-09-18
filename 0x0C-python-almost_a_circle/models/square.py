#!/usr/bin/python3
"""
Module defining a Square class that inherits from Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - a class representing a square, inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square objects"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        if type(value) is not int:
            raise TypeError('Size must be an integer')
        elif value <= 0:
            raise ValueError('Size must be greater than 0')
        self.width = value
        self.height = value

    # Magic methods

    def __str__(self):
        """
        String representation of the Square.
        """
        return ("[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.width))

    # Public methods

    def update(self, *args, **kwargs):
        """
        Update the Square's attributes based on arguments or keyword arguments.

        Args:
            *args: List of arguments.
            **kwargs: Dictionary of arguments, where keys represent
                      attributes of the instance.
        """
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if not args:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id, 'size': self.width}
