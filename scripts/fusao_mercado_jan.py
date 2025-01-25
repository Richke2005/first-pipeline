import json
import csv


path_json = './data_raw/dados_empresaA.json'
path_csv = './data_raw/dados_empresaB.csv'

def reading_json(path_json):
    data_json = []
    with open(path_json, 'r') as file:
        data_json = json.load(file)
    return data_json

def reading_csv(path_csv):
    data_csv: list = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            data_csv.append(row)
    return data_csv

def read_data(path, data_type):
    if data_type == 'json':
        return reading_json(path)
    elif data_type == 'csv':
        return reading_csv(path)
    else:
        print('Tipo de arquivo não suportado')
        return None

dados_json = read_data(path_json, 'json')
dados_csv = read_data(path_csv, 'csv')

print(dados_csv[0])

