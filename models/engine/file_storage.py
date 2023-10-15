#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        projectname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(projectname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        alxdict = FileStorage.__objects
        objdict = {obj: alxdict[obj].to_dict() for obj in alxdict.keys()}
        with open(FileStorage.__file_path, "w") as g:
            json.dump(objdict, g)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as g:
                objdict = json.load(g)
                for p in objdict.values():
                    cls_name = p["__class__"]
                    del p["__class__"]
                    self.new(eval(cls_name)(**p))
        except FileNotFoundError:
            return
