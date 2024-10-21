from fpdf import FPDF


name = input("Name: ")

# Create instance of FPDF class
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Adds an image in the background
pdf.image('shirtificate.png', 0, 50)

# Add a header
pdf.set_font('Arial', 'B', 36)
pdf.cell(0, 25, "CS50 Shirtificate", 0, 1, 'C')

# Add a name
text = f"{name} took CS50"
pdf.set_text_color(255, 255, 255)
pdf.set_font('Arial', 'B', 24)
pdf.cell(0, 200, text, 0, 1, 'C')


pdf.output("shirtificate.pdf")
