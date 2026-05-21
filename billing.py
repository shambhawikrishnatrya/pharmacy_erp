from database import connect_db


def create_bill(customer_name, medicines):

    conn = connect_db()
    cursor = conn.cursor()

    total = 0

    for item in medicines:
        total += item['price'] * item['quantity']

    bill_query = """
    INSERT INTO bills(customer_name, total, bill_date)
    VALUES(%s, %s, NOW())
    """

    cursor.execute(bill_query, (customer_name, total))

    bill_id = cursor.lastrowid

    for item in medicines:

        subtotal = item['price'] * item['quantity']

        item_query = """
        INSERT INTO bill_items
        (bill_id, medicine_id, quantity, subtotal)
        VALUES(%s, %s, %s, %s)
        """

        values = (
            bill_id,
            item['medicine_id'],
            item['quantity'],
            subtotal
        )

        cursor.execute(item_query, values)

        update_query = """
        UPDATE medicines
        SET quantity = quantity - %s
        WHERE id = %s
        """

        cursor.execute(
            update_query,
            (item['quantity'], item['medicine_id'])
        )

    conn.commit()
    conn.close()

    return bill_id