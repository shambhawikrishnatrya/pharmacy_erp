from database import connect_db


def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    conn.close()

    return user
