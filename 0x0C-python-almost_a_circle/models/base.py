#!/usr/bin/python3
"""defines a Base class"""
import json
import csv


class Base:
    """Base class for other project classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize Base instance
        Args:
            - id (int): an id for the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json representaion
        Args:
            -list_dictionaries(list): list of dictionaries
        """
        if (list_dictionaries is None) or (list_dictionaries == []):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of instances in a json file
        Args:
            -list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        dic_list = []
        with open(filename, 'w', encoding="utf-8") as f:
            for obj in list_objs:
                dic_list.append(obj.to_dictionary())
            json_str = Base.to_json_string(dic_list)
            return f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string representaion
        Args:
            -json_string(str): json string
        """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            -dictionary (dict): key/value pairs of attributes
        """
        if cls.__name__ == 'Rectangle':
            dummmy = cls(1, 1)
        else:
            dummmy = cls(1)
        dummmy.update(**dictionary)
        return dummmy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        dic_list = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                read_list = Base.from_json_string(f.read())
                for item in read_list:
                    dic_list.append(cls.create(**item))
                return dic_list
        except IOError:
            return dic_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves data to an csv file"""
        filename = cls.__name__ + ".csv"
        dic_list = []
        with open(filename, 'w', encoding="utf-8") as f:
            if (list_objs is None) or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads data from a csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                dic_list = csv.DictReader(f, fieldnames=fields)
                dic_list = [dict([k, int(v)] for k, v in d.items())
                            for d in dic_list]
                return [cls.create(**d) for d in dic_list]
        except IOError:
            return []
