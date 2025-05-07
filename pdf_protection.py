from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

def create_pdf(file_path):
    # Create a PDF file
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 750, "Hello, this is a protected PDF!")
    c.save()

def protect_pdf(input_pdf_path, output_pdf_path, password):
    # Read the existing PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add password protection
    writer.encrypt(password)

    # Write the protected PDF to a new file
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)

if __name__ == "__main__":
    pdf_file = "example.pdf"
    protected_pdf_file = "protected_example.pdf"
    password = "1234567"

    # Create the PDF
    create_pdf(pdf_file)

    # Protect the PDF
    protect_pdf(pdf_file, protected_pdf_file, password)

    print(f"Created and protected PDF: {protected_pdf_file}")
