from database import connect_db


def add_medicine(name, batch_no, quantity, price, expiry_date):

    conn = connect_db()

    cursor = conn.cursor()

    query = """
    INSERT INTO medicines
    (name, batch_no, quantity, price, expiry_date)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        name,
        batch_no,
        quantity,
        price,
        expiry_date
    )

    cursor.execute(query, values)

    conn.commit()

    conn.close()


def view_medicines():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicines")

    data = cursor.fetchall()

    conn.close()

    print("\n" + "=" * 90)
    print(f"{'ID':<5} {'NAME':<20} {'BATCH':<10} {'QTY':<10} {'PRICE':<10} {'EXPIRY':<15}")
    print("=" * 90)

    for med in data:

        print(
            f"{med[0]:<5} "
            f"{med[1]:<20} "
            f"{med[2]:<10} "
            f"{med[3]:<10} "
            f"{med[4]:<10} "
            f"{med[5]}"
        )

    print("=" * 90)


def delete_medicine(med_id):

    conn = connect_db()

    cursor = conn.cursor()

    query = "DELETE FROM medicines WHERE id=%s"

    cursor.execute(query, (med_id,))

    conn.commit()

    conn.close()
    
    
def reset_medicines():

    conn = connect_db()

    cursor = conn.cursor()

    query = "DELETE FROM medicines"

    cursor.execute(query)

    conn.commit()

    conn.close()

    print("All medicines deleted successfully")
    
    
def sell_medicine(med_id, sold_quantity):

    conn = connect_db()

    cursor = conn.cursor()

    # CHECK CURRENT STOCK
    stock_query = """
    SELECT quantity, name
    FROM medicines
    WHERE id = %s
    """

    cursor.execute(stock_query, (med_id,))

    medicine = cursor.fetchone()

    # IF MEDICINE DOES NOT EXIST
    if medicine is None:

        print("\nMedicine ID not found")

        conn.close()

        return

    current_stock = medicine[0]

    medicine_name = medicine[1]

    # CHECK IF STOCK IS ENOUGH
    if sold_quantity > current_stock:

        print("\nNot enough stock available")

        print(f"Current Stock: {current_stock}")

        conn.close()

        return

    # REDUCE STOCK
    update_query = """
    UPDATE medicines
    SET quantity = quantity - %s
    WHERE id = %s
    """

    cursor.execute(
        update_query,
        (sold_quantity, med_id)
    )

    # CHECK IF MEDICINE EXISTS IN SALES TABLE
    check_query = """
    SELECT *
    FROM sales
    WHERE medicine_name = %s
    """

    cursor.execute(check_query, (medicine_name,))

    existing = cursor.fetchone()

    # UPDATE SALES IF EXISTS
    if existing:

        sales_update = """
        UPDATE sales
        SET quantity_sold = quantity_sold + %s
        WHERE medicine_name = %s
        """

        cursor.execute(
            sales_update,
            (sold_quantity, medicine_name)
        )

    # INSERT NEW SALES RECORD
    else:

        insert_query = """
        INSERT INTO sales
        (medicine_name, quantity_sold)
        VALUES (%s, %s)
        """

        cursor.execute(
            insert_query,
            (medicine_name, sold_quantity)
        )

    conn.commit()

    conn.close()

    print("\nMedicine Sold Successfully")

    print(f"Sold Quantity: {sold_quantity}")

    print(f"Remaining Stock: {current_stock - sold_quantity}")
    
    

def add_stock(med_id, added_quantity):

    conn = connect_db()

    cursor = conn.cursor()

    query = """
    UPDATE medicines
    SET quantity = quantity + %s
    WHERE id = %s
    """

    values = (added_quantity, med_id)

    cursor.execute(query, values)

    conn.commit()

    conn.close()

    print("Stock Updated Successfully")        