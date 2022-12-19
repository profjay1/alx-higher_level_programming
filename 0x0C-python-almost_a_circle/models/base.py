#!/usr/bin/python3
''' Module for Base class '''
import json
import csv


class Base:
    ''' Base object '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns JSON string representation '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes to a file the JSON string representatio '''
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string representation '''
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns a new instance with attrs specified in dictionary '''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        else:
            new = Square(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances loaded from JSON file '''
        import os
        file_path = f"{cls.__name__}.json"
        if not os.path.isfile(file_path):
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' Saves object into csv file '''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]
        with open(f"{cls.__name__}.csv", "w", newline="",
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        ''' Loads an object from csv file '''
        from models.rectangle import Rectangle
        from models.square import Square
        list_objs = list()
        with open(f"{cls.__name__}.csv", "r", newline="",
                  encoding="utf-8") as f:
            file = csv.reader(f)
            for row in file:
                attrs = [int(element) for element in row]
                if cls is Rectangle:
                    d = {"id": attrs[0], "width": attrs[1], "height": attrs[2],
                         "x": attrs[3], "y": attrs[4]}
                else:
                    d = {"id": attrs[0], "size": attrs[1],
                         "x": attrs[2], "y": attrs[3]}
                list_objs.append(cls.create(**d))
        return list_objs
