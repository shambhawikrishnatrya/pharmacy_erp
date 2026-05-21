import mysql.connector


def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anmeshaa",
        database="pharmacy_erp"
    )

    return conn


try:
    conn = connect_db()

    print("Connected to MySQL Successfully")

except Exception as e:
    print("Error:", e)