import matplotlib.pyplot as plt

from database import connect_db


def sales_report():

    conn = connect_db()

    cursor = conn.cursor()

    query = """
    SELECT medicine_name, quantity_sold
    FROM sales
    ORDER BY quantity_sold DESC
    """

    cursor.execute(query)

    data = cursor.fetchall()

    conn.close()

    medicine_names = []
    quantities = []

    for row in data:

        medicine_names.append(row[0])

        quantities.append(row[1])

    plt.figure(figsize=(10, 5))

    plt.bar(medicine_names, quantities)

    plt.xlabel("Medicines")

    plt.ylabel("Quantity Sold")

    plt.title("High Demand Medicines")

    plt.xticks(rotation=20)

    plt.show()


sales_report()