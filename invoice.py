from database import connect_db
from fpdf import FPDF
import os


def generate_invoice(bill_id):

    # Connect to Database
    conn = connect_db()

    # dictionary=True returns data as dictionary
    cursor = conn.cursor(dictionary=True)

    # FETCH BILL INFORMATION

    bill_query = """
    SELECT *
    FROM bills
    WHERE bill_id = %s
    """

    cursor.execute(bill_query, (bill_id,))

    bill = cursor.fetchone()

    # Check if bill exists
    if not bill:
        print("Bill not found!")
        return


    # FETCH MEDICINES IN THAT BILL
    
    items_query = """
    SELECT medicines.name,
           medicines.price,
           bill_items.quantity

    FROM bill_items

    JOIN medicines
    ON medicines.id = bill_items.medicine_id

    WHERE bill_items.bill_id = %s
    """

    cursor.execute(items_query, (bill_id,))

    medicines = cursor.fetchall()

    # CREATE PDF

    pdf = FPDF()

    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 18)

    pdf.cell(
        200,
        10,
        txt="ABC PHARMACY",
        ln=True,
        align='C'
    )

    pdf.ln(10)

    # Customer Details
    pdf.set_font("Arial", size=12)

    pdf.cell(
        200,
        10,
        txt=f"Customer Name: {bill['customer_name']}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Bill ID: {bill['bill_id']}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Total Amount: Rs {bill['total']}",
        ln=True
    )

    pdf.ln(10)

    # TABLE HEADER

    pdf.set_font("Arial", "B", 12)

    pdf.cell(60, 10, "Medicine", 1)
    pdf.cell(40, 10, "Price", 1)
    pdf.cell(40, 10, "Quantity", 1)
    pdf.cell(40, 10, "Subtotal", 1)

    pdf.ln()

    # MEDICINE DATA

    pdf.set_font("Arial", size=12)

    for item in medicines:

        subtotal = item['price'] * item['quantity']

        pdf.cell(60, 10, item['name'], 1)

        pdf.cell(
            40,
            10,
            f"Rs {item['price']}",
            1
        )

        pdf.cell(
            40,
            10,
            str(item['quantity']),
            1
        )

        pdf.cell(
            40,
            10,
            f"Rs {subtotal}",
            1
        )

        pdf.ln()
        
    # FINAL TOTAL

    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)

    pdf.cell(
        200,
        10,
        txt=f"FINAL TOTAL = Rs {bill['total']}",
        ln=True
    )

    # CREATE INVOICE FOLDER

    os.makedirs("invoices", exist_ok=True)

    # SAVE PDF

    file_path = f"invoices/invoice_{bill_id}.pdf"

    pdf.output(file_path)

    # Close DB Connection
    conn.close()

    print(f"Invoice Generated Successfully!")
    print(f"Saved at: {file_path}")


# GENERATE INVOICE

try:

    bill_id = int(input("Enter Bill ID: "))

    generate_invoice(bill_id)

except ValueError:

    print("Please enter valid number")