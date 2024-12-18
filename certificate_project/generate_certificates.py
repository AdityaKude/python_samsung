import os
import pandas as pd
from jinja2 import Template
from weasyprint import HTML

# Function to create a new HTML file from the template
def create_html_from_template(template_file, file_name, context):
    with open(template_file, "r") as template:
        content = template.read()

    # Dynamically adjust the image path (if needed)
    content = content.replace('certificate_bg.jpg', 'static/certificate_bg.jpg')  # Example of replacing background image path

    # Create Jinja2 Template object
    template = Template(content)

    # Render the template with the provided context (name, usn, etc.)
    rendered_html = template.render(**context)

    # Write the rendered HTML to a new file
    with open(file_name, "w") as new_file:
        new_file.write(rendered_html)

    print(f"HTML file {file_name} created successfully.")

    # Convert HTML to PDF
    create_pdf_from_html(file_name)

    return file_name

# Function to convert HTML to PDF using WeasyPrint
def create_pdf_from_html(html_file):
    # Create the PDF file name based on the HTML file name
    pdf_file = html_file.replace('.html', '.pdf')

    # Use WeasyPrint to convert HTML to PDF
    HTML(html_file).write_pdf(pdf_file)

    print(f"PDF file {pdf_file} created successfully.")
    return pdf_file

# Function to process CSV data and create HTML and PDF certificates
def process_csv_data(template_file, csv_file, output_html_dir):
    # Read CSV data
    data = pd.read_csv(csv_file)

    # Create output directory if it doesn't exist
    os.makedirs(output_html_dir, exist_ok=True)

    # Process each row in the CSV
    for index, row in data.iterrows():
        usn = row['USN']
        name = row['Name']

        # Prepare the context for rendering the HTML (name, usn)
        context = {"usn": usn, "name": name}

        # Generate HTML file for each student
        html_file = os.path.join(output_html_dir, f"{usn}.html")
        create_html_from_template(template_file, html_file, context)

# Main program
if __name__ == "__main__":
    # File paths (modify the paths if needed)
    template_file = "template.html"  # Ensure this file exists in your project
    csv_file = "students.csv"       # Ensure this CSV file exists with 'USN' and 'Name' columns
    output_html_dir = "output_htmls" # Directory to save the generated HTML and PDF files

    # Menu-driven system
    print("Choose an option:")
    print("1. Create an HTML file from template and generate PDF")
    print("2. Process a CSV file and generate HTML certificates and PDFs")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        # Option 1: Generate a single HTML file and PDF based on user input
        file_name = input("Enter the name for the new HTML file (without extension): ") + ".html"
        usn = input("Enter USN: ")
        name = input("Enter Name: ")

        # Prepare context for rendering
        context = {"usn": usn, "name": name}

        # Generate the HTML file from the template and create PDF
        create_html_from_template(template_file, file_name, context)
    elif choice == "2":
        # Option 2: Process a CSV file and generate HTML and PDF files for each student
        process_csv_data(template_file, csv_file, output_html_dir)
    else:
        print("Invalid choice. Exiting.")
