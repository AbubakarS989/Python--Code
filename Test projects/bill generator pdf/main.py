from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f"Agreement Between {shop_name} and {party_name}", 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

# Inputs from the user
shop_name = "Hafeez Shoes House"
owner_name = "Abubakar Hafeez"
shop_phone = input("Enter shop phone number: ")
shop_email = input("Enter shop email: ")
shop_address = input("Enter shop address: ")

party_name = input("Enter the name of the second party: ")
party_phone = input("Enter the party's phone number: ")
party_email = input("Enter the party's email: ")
party_address = input("Enter the party's address: ")

scope = input("Enter the scope of the agreement (product/service details): ")
total_cost = input("Enter the total cost: ")
payment_schedule = input("Enter the payment schedule (e.g., 50% upfront, 50% on completion): ")
termination = input("Enter termination details (e.g., written notice, payment conditions): ")

# Create the agreement PDF
pdf = PDF()
pdf.add_page()

# Add content
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, f"Date of Agreement: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
pdf.ln(10)

# Parties Involved
pdf.cell(0, 10, 'Parties Involved:', ln=True)
pdf.multi_cell(0, 10, f"""1. {shop_name}
Owner: {owner_name}
Phone: {shop_phone}
Email: {shop_email}
Address: {shop_address}

2. {party_name}
Phone: {party_phone}
Email: {party_email}
Address: {party_address}
""")

# Scope of Agreement
pdf.ln(5)
pdf.cell(0, 10, 'Scope of Agreement:', ln=True)
pdf.multi_cell(0, 10, f"{scope}")

# Payment Terms
pdf.ln(5)
pdf.cell(0, 10, 'Payment Terms:', ln=True)
pdf.multi_cell(0, 10, f"Total Cost: {total_cost}. Payment Schedule: {payment_schedule}")

# Termination
pdf.ln(5)
pdf.cell(0, 10, 'Termination:', ln=True)
pdf.multi_cell(0, 10, termination)

# Signatures
pdf.ln(10)
pdf.cell(0, 10, 'Signatures:', ln=True)
pdf.cell(0, 10, f'Party 1: {shop_name}: ___________________', ln=True)
pdf.cell(0, 10, f'Party 2: {party_name}: ___________________', ln=True)

# Output the agreement PDF
pdf.output('agreements.pdf')
print("Agreement PDF generated successfully as 'agreement.pdf'")
