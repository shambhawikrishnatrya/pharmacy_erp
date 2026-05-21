from database import connect_db


def add_supplier(name, phone, address):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO suppliers(name, phone, address)
    VALUES(%s, %s, %s)
    """

    cursor.execute(query, (name, phone, address))

    conn.commit()
    conn.close()