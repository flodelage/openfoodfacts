
from database import Database
from settings import DB_NAME

class Manager():
    def __init__(self, parent_class):
        self.parent_class = parent_class
        self.db = Database()

    def save(self, obj):
        table = obj.table # store class' table name
        params = obj.__dict__.keys() # store object's parameters
        args = obj.__dict__.values() # store object's arguments
        columns = ", ".join(params) # set string of params
        values_qty = f"%s, " * len(params) # set number of "%s ," equal to the number of the object's params
        values_qty = values_qty.strip()[:-1:] # remove ending space then ending ","
        if len(params) == 1:
            query = f"INSERT INTO {table} ({columns}) VALUES ('{tuple(args)[0]}')"
            self.db.cursor.execute(query)
        else:
            query = f"INSERT INTO {table} ({columns}) VALUES ({values_qty})"
            values = tuple(args)
            self.db.cursor.execute(query, values)
        self.db.connection.commit()

    def save_all(self, objects_list):
        for obj in objects_list:
            obj_table = obj.table
            obj_insertion = f"""INSERT INTO {obj_table} ({obj.object_attributes_to_str()}) VALUES ({obj.object_values_to_str()})"""
            self.db.cursor.execute(obj_insertion)
            obj_id = "SET @obj_id = LAST_INSERT_ID()"
            self.db.cursor.execute(obj_id)
            for attribute in obj.__dict__.keys():
                if type(obj.__dict__[attribute]) is list:
                    for obj in obj.__dict__[attribute]:
                        obj_2nd_table = obj.table
                        obj_2nd_insertion = f"""INSERT INTO {obj_2nd_table} ({obj.object_attributes_to_str()}) VALUES ({obj.object_values_to_str()}) ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)"""
                        self.db.cursor.execute(obj_2nd_insertion)
                        obj_2nd_id = "SET @obj_2nd_id = LAST_INSERT_ID()"
                        self.db.cursor.execute(obj_2nd_id)
                        # set many_to_many table
                        m_to_m_table = f"{obj_table}_{obj_2nd_table}"
                        m_to_m_insertion = f"""INSERT INTO {m_to_m_table} ({obj_table}_id, {obj_2nd_table}_id) VALUES (@obj_id, @obj_2nd_id)"""
                        self.db.cursor.execute(m_to_m_insertion)
        self.db.connection.commit()

    def columns(self, class_table):
        query = f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{class_table}'"""
        self.db.cursor.execute(query)
        parent_class_cols = self.db.cursor.fetchall()
        return parent_class_cols #[('id',), ('name',)]

    def all(self):
        # set parent class params in dict
        parent_class_params = self.parent_class.params() #{'brand': None, 'category': [], 'name': None, 'nutrition_grade': None, 'stores': None, 'url': None}
        # remove param from parent class params if param is a list
        for key, value in parent_class_params.items():
            if type(value) is list:
                del parent_class_params[key]
                break
        parent_class_table = self.parent_class.table # set parent class table
        # set parent class columns
        if ('id',) in self.columns(parent_class_table):
            parent_class_cols = f"{parent_class_table}.id,"
        else:
            parent_class_cols = f""
        for col, value in parent_class_params.items():
            if type(value) is not list:
                parent_class_cols += f"{self.parent_class.table}.{col}" + ","
        # create query in order to select all the rows of a table
        query = f"""SELECT {parent_class_cols[:-1]} FROM {parent_class_table}""" #SELECT product.id,product.brand,product.name,product.nutrition_grade,product.stores,product.url FROM product
        self.db.cursor.execute(query)
        parent_class_rows = self.db.cursor.fetchall() #[(144, 'Desserts'), (147, 'Frais')]
        # create objects from the statement result
        objects = []
        for row in parent_class_rows:
            if ('id',) in self.columns(parent_class_table):
                id = row[0]
                values = row[1:]
            else:
                values = row
            object_attr_args = [
                (element, values[index])
                for index, element in enumerate(list(parent_class_params.keys()))
            ]
            obj = self.parent_class(**dict(object_attr_args))
            if ('id',) in self.columns(parent_class_table):
                setattr(obj, "id", id)
            objects.append(obj)
        return objects

    def filter(self, **kwargs):
        main_table = self.parent_class.__name__
        main_table_params_dict = self.parent_class.params()
        second_table = ""
        filters = f"""WHERE""" # set up the second part of the query based on past conditions

        for key, value in kwargs.items():
            # check if a second_table exists
            if '__' in key and '__lt' not in key:
                second_table = key[:key.index('_')] # set the second_table name
                condition_key = key.replace('__', '.') # ex: 'category__name' -> 'category.name'
                filters += f" {condition_key} = '{value}' AND "
            # check if a condition 'less_than' exists
            elif '__lt' in key:
                condition_key = key.replace('__lt', '') # ex: 'nutriscore__lt' -> 'nutriscore'
                filters += f" {condition_key} < '{value}' AND "
            else:
                filters += f" {key} = '{value}' AND "
        filters = filters[:-5] # delete the last "AND"

        # set up the first part of the query depending on whether there is a second table or not
        if second_table != "": # if there is a second table
            second_table_params = self.columns(second_table)
            main_table_elements = f"{main_table}.id,"
            second_table_elements = f""
            for param in main_table_params_dict.keys():
                if param == second_table:
                    next
                else:
                    main_table_elements += f"{main_table}.{param},"
            for param in second_table_params:
                second_table_elements += f"{second_table}.{param[0]},"
            select = f"""SELECT {main_table_elements}{second_table_elements[:-1]}
                         FROM {main_table}
                         INNER JOIN {main_table}_{second_table}
                         ON {main_table}_{second_table}.{main_table}_id = {main_table}.id
                         INNER JOIN {second_table} ON {second_table}.id = {main_table}_{second_table}.{second_table}_id"""
        else: # if there is not a second table
            select_elements = f"{main_table}.id,"
            for param, value in main_table_params_dict.items():
                if type(value) is not list:
                    select_elements += f"{main_table}.{param},"
            select = f"""SELECT {select_elements[:-1]} FROM {main_table}"""

        query = select + " " + filters # add first and second part of the query in order to set up the final query

        self.db.cursor.execute(query)
        rows = self.db.cursor.fetchall()

        # create objects from the statement result
        for key, value in main_table_params_dict.items():
            if type(value) is list:
                del main_table_params_dict[key]
                break

        objects = []
        for row in rows:
            id = row[0]
            values = row[1:]
            object_attr_args = [
                (element, values[index])
                for index, element in enumerate(list(main_table_params_dict.keys()))
            ]
            obj = self.parent_class(**dict(object_attr_args))
            setattr(obj, "id", id)
            objects.append(obj)
        return objects

    def delete(self, **kwargs):
        main_table = self.parent_class.__name__
        filters = "".join(f"{key} = {value} AND " for key, value in kwargs.items())
        query = f"DELETE FROM {main_table} WHERE {filters[:-5]}"
        self.db.cursor.execute(query)
        self.db.connection.commit()
