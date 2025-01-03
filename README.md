# CLI Currency

A command-line interface (CLI) application for managing and monitoring currency information. This application allows you to add currencies, list them with various filters and sorting options, and generate reports on the minimum and maximum values of each currency.

## Features

- **Add Currency**: Add a new currency with its value.
- **List Currencies**: List all currencies with options to filter by name and sort by value or date.
- **Report**: Generate a report showing the minimum and maximum values of each currency.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/aminhat/cli_currency.git
   cd cli_currecy
2. **create a virtual enviroment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
4. **Set up the PostgreSQL database**:
   - Ensure PostgreSQL is installed and running.
   
## Usage
- ##### Add a Currency
    To add a new currency, use the ```add``` command:
    ```sh
    python main.py add <name> <value>
    ```
    Example:
    ```
    python main.py add USD 1.00
    ```
- ##### List Currencies

    To list all currencies, use the ```list``` command:
    ```sh
    python main.py list
    ```
    You can also filter and sort the list using ```-f``` and ```-s``` flags:
    
    - ##### Filter by name:
    
        ```sh
        python main.py list -f <filter_name>
        ```
    - ##### sort by ```--price``` or ```--date```:
    
        ```sh
        python main.py list -s --asc --date 
        python main.py list -s --desc  # Sort by value (default)
        ```
- ##### Generate Report
    To generate a report showing the minimum and maximum values of each currency, use the report command:
    ```sh
    python main.py report
    ```
    
    ##### _also you can use ```-h``` on all command to get help_
    
## Example
You can use the WATCHME.cast file with the asciinema command to see an example of how to use the CLI:
- Install asciinema:
    ```
    brew install asciinema  # On macOS
    sudo apt-get install asciinema  # On Ubuntu
    ```
- Play the example:
    ```
    asciinema play WATCHME.cast
    ``` 


    