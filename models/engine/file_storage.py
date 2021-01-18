#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models


class FileStorage():
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        new_dict = {}
        if cls is None:
            return self.__objects

        if cls != "":
            for kay, value in self.__objects.items():
                if cls == key.split(".")[0]:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """Saves storage dictionary to file"""
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, value in FileStorage.__objects.items():
                class_name = value["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an obj"""
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            FileStorage.__objects.pop(key, None)
            self.save()
