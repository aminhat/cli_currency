def main():
    import argparse
    from cli.commands import add, listc, report

    parser = argparse.ArgumentParser(description='My Python CLI Application')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a currency')
    add_parser.add_argument('name', type=str, help='Name of currency')
    add_parser.add_argument('value', type=float, help='Value of currency')

    list_parser = subparsers.add_parser('list', help='List all currencies')
    list_parser.add_argument('-f', '--filter', action='store_true', help='Filter by name')
    list_parser.add_argument('filter_name', type=str, nargs='?', help='Name of currency to be filtered')
    list_parser.add_argument('-s', '--sort', action='store_true', help='Sort output by value')
    list_parser.add_argument('--asc', action='store_true', help='Sort in ascending order')
    list_parser.add_argument('--desc', action='store_true', help='Sort in descending order')
    list_parser.add_argument('--price', action='store_true', help='Sort by value')
    list_parser.add_argument('--date', action='store_true', help='Sort by date created at')

    report_parser = subparsers.add_parser('report', help='Report min and max value of each currency')

    args = parser.parse_args()

    if args.command == 'add': 
        add(args.name, args.value)
    elif args.command == 'list': 
        listc(args.filter_name if args.filter else '',
            args.sort,
            'ASC' if args.asc else 'DESC', 
            'created_at' if args.date else 'value')
    elif args.command == 'report':
        report()

if __name__ == '__main__':
    main()