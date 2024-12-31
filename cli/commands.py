import csv
import datetime
import uuid
from cli.mydb import getdata_db, postdata_db

def add(name, values):
    postdata_db("INSERT INTO currencies (name, value) VALUES (%s, %s)", (name, values))

def list_all(sort, order):
    data = getdata_db(f"SELECT name, value FROM currencies ORDER BY value {order}" if sort else "SELECT name, value FROM currencies")

    for row in data:
        print(f'Name: {row[0]}, Value: {row[1]}')
              
def list_filter(name, sort, order):
    data = getdata_db(f"SELECT name, value FROM currencies WHERE name = '{name}' ORDER BY value {order}" if sort else f"SELECT name, value FROM currencies WHERE name = '{name}'")

    print(f"prices for {name}:")
    for row in data:
        print(row[1])
        
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