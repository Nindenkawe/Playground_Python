import re
from PyPDF2 import PdfReader

def extract_minutes_from_pdf(pdf_file_path):
    total_minutes = 0

    try:
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)

            for page_num in range(len(pdf_reader.pages)):
                text = pdf_reader.pages[page_num].extract_text()

                # Use regular expression to find and extract minutes
                minutes_matches = re.findall(r'\b(\d+)\s*minutes?\b', text, re.IGNORECASE)

                # Sum the extracted minutes
                for match in minutes_matches:
                    total_minutes += int(match)

        return total_minutes

    except FileNotFoundError:
        print(f"Error: File '{pdf_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = 'exerciseB/File_manupulation/minutes_hist115.pdf'
total_minutes = extract_minutes_from_pdf(pdf_file_path)

if total_minutes is not None:
    print(f'Total minutes: {total_minutes}')
