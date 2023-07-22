import csv
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
