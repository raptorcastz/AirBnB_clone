#!/usr/bin/python3
"""basemodel class definition"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """for the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel.
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for a, c in kwargs.items():
                if a == "created_at" or a == "updated_at":
                    self.__dict__[a] = datetime.strptime(c, timeformat)
                else:
                    self.__dict__[a] = c
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    @property
    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        classicname = self.__class__.__name__
        return "[{}] ({}) {}".format(classicname, self.id, self.__dict__)