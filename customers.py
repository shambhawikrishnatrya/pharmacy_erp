from database import connect_db


def add_customer(name, phone):

    conn = connect_db()
    cursor = conn.cursor()

    query = "INSERT INTO customers(name, phone) VALUES(%s, %s)"

    cursor.execute(query, (name, phone))

    conn.commit()
    conn.close()