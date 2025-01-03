def main():
    import argparse
    import configparser
    import psycopg2
    from cli.commands import add_currency, listـcurrencies, report_min_max_currencies

    config = configparser.ConfigParser()
    config.read('db.conf')
    db_config = config['database']
    conn = psycopg2.connect(
        host=db_config['host'],
        port=db_config['port'],
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()

    parser = argparse.ArgumentParser(description='My Python CLI Application about currencies')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a currency')
    add_parser.add_argument('name', type=str, help='Name of currency')
    add_parser.add_argument('value', type=float, help='Value of currency')

    list_parser = subparsers.add_parser('list', help="List all currencies")
    list_parser.add_argument('-f', '--filter', action='store_true', help='Filter by name')
    list_parser.add_argument('filter_name', type=str, nargs='?', help='Name of currency to be filtered')
    list_parser.add_argument('-s', '--sort', action='store_true', help='Sort output by value or date')
    list_parser.add_argument('--asc', action='store_true', help='Sort in ascending order')
    list_parser.add_argument('--desc', action='store_true', help='Sort in descending order (default)')
    list_parser.add_argument('--price', action='store_true', help='Sort by value (default)')
    list_parser.add_argument('--date', action='store_true', help='Sort by date created at')

    report_parser = subparsers.add_parser('report', help='Report minimum and maximum value of each currency')

    args = parser.parse_args()

    if args.command == 'add': 
        add_currency(args.name, args.value, cursor)
    elif args.command == 'list': 
        listـcurrencies(args.filter_name if args.filter else '',
            args.sort,
            'ASC' if args.asc else 'DESC', 
            'created_at' if args.date else 'value', 
            cursor)
    elif args.command == 'report':
        report_min_max_currencies(cursor)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()


    