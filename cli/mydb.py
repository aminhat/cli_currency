import psycopg2

def getdata_db(query):
    conn = psycopg2.connect("dbname=cli_currency user=admin host=localhost port=5432 password=Mn8bV44C")
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data

def postdata_db(query, values):
    conn = psycopg2.connect("dbname=cli_currency user=admin host=localhost port=5432 password=Mn8bV44C")
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
