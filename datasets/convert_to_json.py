import csv
import json

DATA_ADS = 'ads.csv'
JSON_ADS = 'ads.json'
DATA_CATEGORIES = 'categories.csv'
JSON_CATEGORIES = 'categories.json'


def convert_to_json(csv_file, json_file, model):
    result = []
    with open(csv_file) as csv_f:
        for row in csv.DictReader(csv_f):
            to_add = {'model': model, 'pk': int(row['id']), 'fields': row}
            if 'id' in row:
                del row['id']
            if row['is_published'] == 'TRUE':
                row['is_published'] = True
            elif row['is_published'] == 'FALSE':
                row['is_published'] = False
            if 'price' in row:
                row['price'] = int(row['price'])
            result.append(to_add)
    with open(json_file, 'w') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


convert_to_json(DATA_CATEGORIES, JSON_CATEGORIES, 'ads.category')
convert_to_json(DATA_ADS, JSON_ADS, 'ads.ads')
