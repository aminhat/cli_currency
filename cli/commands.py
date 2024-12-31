from cli.mydb import getdata_db, postdata_db
from termcolor import colored

def add(name, values):
    postdata_db("INSERT INTO currencies (name, value) VALUES (%s, %s)", (name, values))

def listc(filter_name, is_sorted, sort_order):
    sort_query = f"ORDER BY value {sort_order}" if is_sorted else ""
    filter_query = f"WHERE name = '{filter_name}'" if filter_name != "" else ""
    data = getdata_db(f"SELECT name, value FROM currencies {filter_query} {sort_query}")
    
    print(colored(f"{'Name':<10}{'Value':<10}", 'green'))
    for row in data:
        print(f"{row[0]:<10}{row[1]:<10}")

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