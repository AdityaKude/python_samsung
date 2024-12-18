import os
import pandas as pd
from jinja2 import Template

# Function to create a new HTML file from the template
def create_html_from_template(template_file, file_name, context):
    with open(template_file, "r") as template:
        content = template.read()
    template = Template(content)
    rendered_html = template.render(**context)
    with open(file_name, "w") as new_file:
        new_file.write(rendered_html)
    print(f"HTML file {file_name} created successfully.")
    return file_name

# Function to process CSV data and create HTML certificates
def process_csv_data(template_file, csv_file, output_html_dir):
    # Read CSV data
    data = pd.read_csv(csv_file)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_html_dir, exist_ok=True)
    
    # Process each row in the CSV
    for index, row in data.iterrows():
        usn = row['USN']
        name = row['Name']
        context = {"usn": usn, "name": name}
        
        # Generate HTML file
        html_file = os.path.join(output_html_dir, f"{usn}.html")
        create_html_from_template(template_file, html_file, context)

# Main program
if __name__ == "__main__":
    # File paths
    template_file = "template.html"
    csv_file = "students.csv"
    output_html_dir = "output_htmls"
    
    # Menu-driven system
    print("Choose an option:")
    print("1. Create an HTML file from template")
    print("2. Process a CSV file and generate HTML certificates")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        file_name = input("Enter the name for the new HTML file (without extension): ") + ".html"
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        context = {"usn": usn, "name": name}
        create_html_from_template(template_file, file_name, context)
    elif choice == "2":
        process_csv_data(template_file, csv_file, output_html_dir)
    else:
        print("Invalid choice. Exiting.")
