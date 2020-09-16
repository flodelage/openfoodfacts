
from database import Database


class Manager():
    def __init__(self, parent_class):
        self.parent_class = parent_class
        self.db = Database()

    def save(self, obj):
        table = obj.table # store Product's table name
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
            obj_columns = ""
            obj_values = ""
            for attribute in obj.__dict__.keys():
                if type(obj.__dict__[attribute]) is not list:
                    # set object's table:
                    obj_table = obj.table
                    # set object's columns:
                    obj_columns += attribute + "," # add each attribute to the columns string
                    # set object's values:
                    obj_values += f""" "{obj.__dict__[attribute].strip()}" """ + "," # add each value to the values string
                else:
                    obj_insertion = f"""INSERT INTO {obj_table} ({obj_columns[:-1:]}) VALUES ({obj_values[:-1:]})"""
                    self.db.cursor.execute(obj_insertion)
                    obj_id = "SET @obj_id = LAST_INSERT_ID()"
                    self.db.cursor.execute(obj_id)
                    for obj in obj.__dict__[attribute]:
                        obj_2nd_columns = ""
                        obj_2nd_values = ""
                        for attribute in obj.__dict__.keys():
                            # set object's table:
                            obj_2nd_table = obj.table
                            # set object's columns:
                            obj_2nd_columns += attribute + "," # add each attribute to the columns string
                            # set object's values:
                            obj_2nd_values += f""" "{obj.__dict__[attribute].strip()}" """ + "," # add each value to the values string
                        obj_2nd_insertion = f"""INSERT INTO {obj_2nd_table} ({obj_2nd_columns[:-1:]}) VALUES ({obj_2nd_values[:-1:]}) ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id)"""
                        self.db.cursor.execute(obj_2nd_insertion)
                        obj_2nd_id = "SET @obj_2nd_id = LAST_INSERT_ID()"
                        self.db.cursor.execute(obj_2nd_id)
                        # set many_to_many table
                        m_to_m_table = f"{obj_table}_{obj_2nd_table}"
                        m_to_m_insertion = f"""INSERT INTO {m_to_m_table} ({obj_table}_id, {obj_2nd_table}_id) VALUES (@obj_id, @obj_2nd_id)"""
                        self.db.cursor.execute(m_to_m_insertion)
        self.db.connection.commit()

    def columns(self, table_name):
        query = f"""SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"""
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
        parent_class_cols = f"{parent_class_table}.id,"
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
            id = row[0]
            values = row[1:]
            object_attr_args = [
                (element, values[index])
                for index, element in enumerate(list(parent_class_params.keys()))
            ]
            obj = self.parent_class(**dict(object_attr_args))
            setattr(obj, "id", id)
            objects.append(obj)
        return objects

    def filter(self, **kwargs):
        for key in kwargs.keys():
            if '__' in key:
                main_table = self.parent_class.__name__
                second_table = key[:key.index('_')]



        # parent_class_cols = self.columns() #[('id',), ('name',)]
        # cols = ""
        # for col in parent_class_cols:
        #     cols += col[0] + ","

        # query = f"""SELECT * FROM {self.parent_class.__name__} WHERE {column} = '{value}'"""
        # self.db.cursor.execute(query)
        # result = self.db.cursor.fetchall() #[(144, ' Desserts'), (147, ' Frais')]

        # objects = []
        # for row in result:
        #     id = row[0]
        #     values = ",".join(row[-1:])
        #     obj = self.parent_class(values)
        #     obj.id = id
        #     objects.append(obj)
        # return objects
