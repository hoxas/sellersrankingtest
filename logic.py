"""
Register sales on the database interactively

Usage:
python3 logic.py [arg]
python logic.py [arg]

Leave with no arg for default registration process.
Args:
-h --help           Display this string and exit
-s --skip           Skips sale registration process and outputs list
-l --list           Lists registered sellers and exit
"""
import sqlite3 as sql
import datetime as dt
import sys

def db_connect(db = 'db.db') -> tuple:
    """
    Connect to database

    Args:
        db (string, optional): Path to database file

    Returns:
        Tuple containing (sql.Connection, sql.Cursor)
    """

    connection = sql.connect(db)
    cursor = connection.cursor()
    print("Connection established!")
    return (connection, cursor)

def register(cursor: sql.Cursor) -> None:
    """
    Register a new sale on the database

    Args:
        cursor (sql.Cursor): Cursor to perform queries to db
    """

    seller_name = input('Enter seller name: ')

    response = cursor.execute(f'SELECT id, name FROM sellers WHERE name="{seller_name}"')
    target = response.fetchone()
    if target is None:
        print(f'Seller Name: {seller_name} - Not Found')
        return register(cursor)
    
    seller_id, seller_name = target
    customer = input('Enter customer name: ')

    date = input('Enter date dd/mm/yy (leave blank for today): ')
    if not date:
        date = dt.datetime.today()
    else:
        date = dt.datetime.strptime(date, '%d/%m/%y')
    
    item = input('Enter item name: ')
    
    value = input('Enter item value: ')
    value = float(value.replace(',','.'))
    
    response = cursor.execute(f'INSERT INTO sales(seller, customer, date, item, value) VALUES({seller_id}, "{customer}", {date.timestamp()}, "{item}", {value})')

def display(cursor: sql.Cursor) -> None:
    """
    Prints sellers ranking

    Args:
        cursor (sql.Cursor): Cursor to perform queries to db
    """

    """
    Ok this is what I got from the required output written on the pdf file as: 
    "the output is printed as an updated list of all sales
    registered, sorted by sellers with the highest to lowest amount sold." 

    -> So group the sales by sellers and order them by seller with most sales <-
    """
    response = cursor.execute('SELECT sales.*, sellers.name, counter.count FROM sales LEFT JOIN (SELECT sales.seller, count(sales.seller) as count FROM sales GROUP BY sales.seller) counter ON counter.seller = sales.seller INNER JOIN sellers ON sales.seller = sellers.id ORDER BY counter.count DESC')
    print("All sales, sorted by sellers with most sales, descending:")
    for row in response:
        customer, date, item, price, seller = row[2:-1]
        sale = {'customer': customer, 'date': date, 'item': item, 'price': price, 'seller_name': seller}
        print(sale)

def display_sellers(cursor: sql.Cursor) -> None:
    """
    Print registered sellers names

    Args:
        cursor (sql.Cursor): Cursor to perform queries to db
    """
    response = cursor.execute('SELECT name FROM sellers')
    for row in response:
        print(row[0])

def argument_parse(arg_list: list) -> bool:
    """
    Receives list of arguments and checks for matches

    Args:
        arg_list (list): List of strings containing arguments to match
    
    Returns:
        Boolean true if matches found and false if not found
    """
    return any(arg in sys.argv[1:] for arg in arg_list)

def main():
    if argument_parse(['-h', '--help']):
        return print(__doc__);

    print('Opening Sale Registration')

    print('Connecting to DB... ')
    connection, cursor = db_connect()

    if argument_parse(['-s', '--skip']): 
        print('Skipping registration process')
    elif argument_parse(['-l', '--list']):
        print('Listing registered sellers: ')  
        display_sellers(cursor)
    else:
        print('Starting Interactive Sale Registration')
        try:
            register(cursor)
        except Exception as err:
            print(f'Error: {err}')
        else:
            connection.commit()
    
    if not argument_parse(['-l', '--list']):
        display(cursor)

    connection.close()
    
if __name__ == "__main__":
    main()
