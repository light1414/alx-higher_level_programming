#!/usr/bin/python3
'''Square class module.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class rep.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Starts a new square.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Prints string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''square size.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''the internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''current instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''prints dictionary rep of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
