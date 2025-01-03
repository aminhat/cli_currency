# from cli.mydb import getـdata_db, post_data_db
from termcolor import colored

def add_currency(name, value, cursor):
    cursor.execute("INSERT INTO currencies (name, value) VALUES (%s, %s)", (name, value))
    
def listـcurrencies(filter_name, is_sorted, sort_order, sort_by, cursor):
    sort_query = f"ORDER BY {sort_by} {sort_order}" if is_sorted else ""
    filter_query = f"WHERE name = '{filter_name}'" if filter_name != "" else ""
    cursor.execute(f"SELECT name, value FROM currencies {filter_query} {sort_query}")
    data = cursor.fetchall()
    
    print(colored(f"{'Name':<10}{'price':<10}", 'green'))
    for row in data:
        print(f"{row[0]:<10}{row[1]:<10}")

def report_min_max_currencies(cursor):
    cursor.execute("SELECT name, value FROM currencies")
    data = cursor.fetchall()
    currency_data = {}
    for row in data:
        name = row[0]
        value = float(row[1])
        if name not in currency_data:
            currency_data[name] = []
        currency_data[name].append(value)
    
    print(colored(f"{'Currency':<10}{'Min price':<11}{'Max price':<10}", 'green'))
    for name, values in currency_data.items():
        print(f"{name:<10}{min(values):<11}{max(values):<10}")

