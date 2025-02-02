__package__ = 'scripts'

import json 
import csv

class Data:
    
    def __init__(self, path, data_type):
        self.path = path
        self.type = data_type
        self.data = self.__read_data()
        self.collum_names = self.__get_collums()

    @property     
    def size(self):
        return len(self.data)
    
    def __str__(self):
        return f'Path: {self.path}, Type: {self.type}'
    
    # Extract methods
    def __reading_json(self):
        data_json = []
        with open(self.path, 'r') as file:
            data_json = json.load(file)
        return data_json

    def __reading_csv(self):
        data_csv: list = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                data_csv.append(row)
        return data_csv

    def __read_data(self):
        data: list = []
        if self.type == 'json':
            data = self.__reading_json()
        elif self.type == 'csv':
            data = self.__reading_csv()
        elif self.type == 'list':
            data = self.path
            self.path = 'list at memory'

        return data
        
    def __get_collums(self):
        return list(self.data[-1].keys())

    def rename_collums(self, key_mapping):
        new_data: list = []

        for old_dict in self.data:
            dict_temp: dict = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)
        self.data = new_data
        self.collum_names = self.__get_collums()

    def join(data_A, data_B):
        combined_list: list = []
        combined_list.extend(data_A.data)
        combined_list.extend(data_B.data)
        return Data(combined_list, 'list')
    
    def __transform_data_to_table(self):
        table_combined_data = [self.collum_names]

        for row in self.data:
            line = []
            for comllum in self.collum_names:
                line.append(row.get(comllum, 'Indisponível'))
            table_combined_data.append(line)
        return table_combined_data


    def saving_data(self, path):
        table_combined_data = self.__transform_data_to_table()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(table_combined_data)

