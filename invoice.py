from fpdf import FPDF


def generate_invoice(customer_name, medicines, total, bill_id):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="ABC PHARMACY", ln=True, align='C')

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Customer: {customer_name}", ln=True)

    pdf.cell(200, 10, txt=f"Bill ID: {bill_id}", ln=True)

    pdf.ln(10)

    for item in medicines:
        line = f"{item['name']} x {item['quantity']} = Rs {item['price'] * item['quantity']}"
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.ln(10)

    pdf.cell(200, 10, txt=f"TOTAL = Rs {total}", ln=True)

    pdf.output(f"invoices/invoice_{bill_id}.pdf")