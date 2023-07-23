""" import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read CSV data
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write JSON data
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Replace 'input.csv' with the path to your CSV file and 'output.json' with the desired JSON file path
    csv_to_json('exerciseB/Csv_manupulation/Insurance.csv', 'Insurance.json')
 """


import requests
import pandas as pd
import json

def download_csv_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for successful response
    return response.text

def csv_to_json(csv_data):
    # Load CSV data into a pandas DataFrame
    df = pd.read_csv(pd.compat.StringIO(csv_data))

    # Convert DataFrame to a list of dictionaries and then to JSON
    json_data = df.to_dict(orient='records')

    return json_data

def save_json_to_file(json_data, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    url = 'https://www.statistics.gov.rw/statistical-publications/subject/capital-market'  # Replace with the URL of the CSV file you want to download
    json_file_path = 'output.json'

    try:
        csv_data = download_csv_from_url(url)
        json_data = csv_to_json(csv_data)
        save_json_to_file(json_data, json_file_path)
        print("CSV data converted and saved to JSON successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the CSV data: {e}")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV data with pandas: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
