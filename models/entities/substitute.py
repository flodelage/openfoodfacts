
import unidecode
import inspect
from exceptions import ModelHasNoAttributeWhichIsNotList
from models.entities.product import Product
from models.manager import Manager

class Substitute():
    table = "substitute"
    product = []

    def __init__(self, product=None):
        self.product = product
        if isinstance(self.product, Product):
            prod = self.product
            self.product = []
            self.product.append(prod)

    def object_attributes_to_str(self):
        obj_columns = ""
        for attribute in self.__dict__.keys():
            if type(self.__dict__[attribute]) is not list:
                obj_columns += attribute + ","
        return obj_columns[:-1:]

    def object_values_to_str(self):
        obj_values = ""
        for attribute in self.__dict__.keys():
            if type(self.__dict__[attribute]) is not list:
                obj_values += f""" "{self.__dict__[attribute].strip()}" """ + ","
        return obj_values[:-1:]

    @classmethod
    def params(cls):
        attributes = inspect.getmembers(cls, lambda attr:not(inspect.isroutine(attr)))
        filtered_attributes = dict( [attr for attr in attributes if not(attr[0].startswith('__') and attr[0].endswith('__'))] )
        return {
            key: value
            for key, value in filtered_attributes.items()
            if value is None or (isinstance(value, list) == True)
        }


Substitute.objects = Manager(Substitute)