import csv
import datetime
import uuid
from cli.mydb import getdata_db, postdata_db

def add(name, values):
    postdata_db("INSERT INTO currencies (name, value) VALUES (%s, %s)", (name, values))

def list_all(sort, order):
    data = getdata_db(f"SELECT * FROM currencies ORDER BY value {order}" if sort else "SELECT * FROM currencies")

    for row in data:
        print(f'Name: {row[1]}, Value: {row[2]}')
              
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