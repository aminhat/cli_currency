import csv
import datetime
import uuid

def add(name, value):
    unique_id = str(uuid.uuid4())
    with open('database.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([unique_id, name, value, datetime.datetime.now()])

def list_all(sort):
    with open('database.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if sort:
            rows.sort(key=lambda x: x[2])
        for row in rows:
            print(f'Name: {row[1]}, Value: {row[2]}, Date added: {row[3]}')

def list_filter(name, sort):
    with open('database.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if sort:
            rows.sort(key=lambda x: x[2])
        for row in rows:
            if row[1] == name:
                print(f'Name: {row[1]}, Value: {row[2]}, Date added: {row[3]}')

def report():
    with open('database.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        currency_data = {}

        for row in reader:
            name = row[1]
            value = float(row[2])
            if name not in currency_data:
                currency_data[name] = []
            currency_data[name].append(value)

        for name, values in currency_data.items():
            min_value = min(values)
            max_value = max(values)
            print(f'Currency: {name}, Min Value: {min_value}, Max Value: {max_value}')