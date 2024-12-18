import os
import pandas as pd
from jinja2 import Template
from weasyprint import HTML
from datetime import datetime

# Function to create HTML from the template and generate a PDF
def create_html_and_pdf(template_file, file_name, context):
    # Read the template file
    with open(template_file, "r") as template:
        content = template.read()

    # Get the absolute paths for the background, signature, and logo images
    bg_image_path = os.path.abspath(r"C:\Users\Administrator\Documents\learning\python\python_samsung\certificate_project\certificate_bg.jpg")
    signature_image_path = os.path.abspath(r"C:\Users\Administrator\Documents\learning\python\python_samsung\certificate_project\my_sign.jpg")
    logo_image_path = os.path.abspath(r"C:\Users\Administrator\Documents\learning\python\python_samsung\certificate_project\mtd.png")

    # Format paths as file://
    context["bg_image"] = f"file:///{bg_image_path.replace(os.sep, '/')}"
    context["signature_image"] = f"file:///{signature_image_path.replace(os.sep, '/')}"
    context["logo_image"] = f"file:///{logo_image_path.replace(os.sep, '/')}"

    # Render the template with Jinja2
    template = Template(content)
    rendered_html = template.render(**context)

    # Write the rendered HTML to a new file
    with open(file_name, "w") as new_file:
        new_file.write(rendered_html)
    print(f"HTML file {file_name} created successfully.")

    # Convert HTML to PDF
    create_pdf_from_html(file_name)

# Function to convert an HTML file to PDF
def create_pdf_from_html(html_file):
    pdf_file = html_file.replace(".html", ".pdf")
    HTML(html_file).write_pdf(pdf_file)
    print(f"PDF file {pdf_file} created successfully.")

# Function to process CSV data and generate certificates
def process_csv_data(template_file, csv_file, output_html_dir):
    # Read CSV data
    data = pd.read_csv(csv_file)

    # Create output directory if it doesn't exist
    os.makedirs(output_html_dir, exist_ok=True)

    # Process each row in the CSV
    for index, row in data.iterrows():
        usn = row['USN']
        name = row['Name']
        date = datetime.now().strftime("%d %B %Y")  # Current date

        # Prepare context for rendering
        context = {"usn": usn, "name": name, "date": date}

        # Generate HTML file and PDF
        html_file = os.path.join(output_html_dir, f"{usn}.html")
        create_html_and_pdf(template_file, html_file, context)

# Main program
if __name__ == "__main__":
    # File paths
    template_file = "template.html"  # Updated to match the root folder structure
    csv_file = "students.csv"
    output_html_dir = "output"

    # Menu-driven system
    print("Choose an option:")
    print("1. Create an HTML file from template and generate PDF")
    print("2. Process a CSV file and generate HTML certificates and PDFs")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        # Option 1: Generate a single certificate
        file_name = input("Enter the name for the HTML file (without extension): ") + ".html"
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        date = datetime.now().strftime("%d %B %Y")

        # Prepare context for rendering
        context = {"usn": usn, "name": name, "date": date}

        # Generate certificate
        create_html_and_pdf(template_file, file_name, context)
    elif choice == "2":
        # Option 2: Process a CSV file
        process_csv_data(template_file, csv_file, output_html_dir)
    else:
        print("Invalid choice. Exiting.")
