import configparser
import psycopg2

class DB:
    conn = None
    cursor = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('db.conf')
        db_config = config['database']
        DB.conn = psycopg2.connect(
            host=db_config['host'],
            port=db_config['port'],
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password']
        )
        DB.cursor = DB.conn.cursor()

    def __del__(self):
        DB.cursor.close()
        DB.conn.close()

    def execute(self, query, values): # posting data
        DB.cursor.execute(query, values)

    def execute(self, query):         # getting data
        DB.cursor.execute(query)

    def commit(self):
        DB.conn.commit()

    def fetchall(self):
        return DB.cursor.fetchall()

    def fetchone(self):
        return DB.cursor.fetchone()

