""" import requests
from bs4 import BeautifulSoup
import json

def scrape_specific_data(url, timeout=10):
    try:
        # Send a GET request to the specified URL with a timeout
        response = requests.get(url, timeout=timeout)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Identify the HTML elements containing the specific data
            data_block = soup.find('div', class_='entity-publication')

            # Prepare a dictionary to store extracted data
            data = {}

            if data_block:
                # Extract relevant information from the data block
                data['Figure Name'] = data_block.find('h2').text.strip()
                data['Figure Unit'] = data_block.find('div', class_='field-name-field-pub-fig-unit').text.strip()
                data['Figure Value'] = data_block.find('div', class_='col-md-3').find('h2').text.strip()

                # Check if there are at least two div elements
                div_elements = data_block.find('div', class_='col-md-3').find_all('div')
                if len(div_elements) > 1:
                    data['Figure Period'] = div_elements[1].text.strip()
                else:
                    data['Figure Period'] = None  # Handle the case where the element is not present

                # Additional information (optional)
                source_elem = data_block.find('div', class_='field-name-field-pub-pubsource')
                data['Source'] = source_elem.find('a')['href'] if source_elem else None

            return data
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
            return None

    except requests.Timeout:
        print("Error: Request timed out.")
        return None

if __name__ == "__main__":
    # Replace 'YOUR_SPECIFIC_URL' with the actual URLs of the pages containing the specific data
    urls = [
        'https://www.statistics.gov.rw/publication/gross-domestic-product',
        'https://www.statistics.gov.rw/publication/consumer-price-index',
        'https://www.statistics.gov.rw/publication/life-expectancy-birth',
        'https://www.statistics.gov.rw/publication/size-resident-population'
    ]

    # List to store results for each URL
    all_data = []

    for url in urls:
        # Scrape specific data and append to the list
        specific_data = scrape_specific_data(url, timeout=5)
        if specific_data:
            all_data.append(specific_data)

    # Save the accumulated data to a single JSON file
    with open('exerciseB/fastapi/general_stats.json', 'w') as json_file:
        json.dump(all_data, json_file, indent=2)

    print(f"Data for all URLs saved to 'general_stats.json'")
 """


import requests
from bs4 import BeautifulSoup
import json

def scrape_specific_data(url, timeout=10):
    try:
        # Send a GET request to the specified URL with a timeout
        response = requests.get(url, timeout=timeout)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Identify the HTML elements containing the specific data
            data_block = soup.find('div', class_='entity-publication')

            # Prepare a dictionary to store extracted data
            data = {}

            if data_block:
                # Extract relevant information from the data block
                data['Name'] = data_block.find('h2').text.strip()
                data['Unit'] = data_block.find('div', class_='field-name-field-pub-fig-unit').text.strip()
                data['Value'] = data_block.find('div', class_='col-md-3').find('h2').text.strip()

                # Check if there are at least two div elements
                div_elements = data_block.find('div', class_='col-md-3').find_all('div')
                if len(div_elements) > 1:
                    data['Period'] = div_elements[1].text.strip()
                else:
                    data['Period'] = None  # Handle the case where the element is not present

                # Additional information (optional)
                source_elem = data_block.find('div', class_='field-name-field-pub-pubsource')
                data['Source'] = source_elem.find('a')['href'] if source_elem else None

                # Use Source as the primary key
                data.pop('Figure Name', None)  # Remove unnecessary key
                data.pop('Figure Unit', None)  # Remove unnecessary key
                data.pop('Figure Value', None)  # Remove unnecessary key
                data.pop('Figure Period', None)  # Remove unnecessary key

            return data
        else:
            # Print an error message if the request was not successful
            print(f"Error: Unable to fetch the content. Status code: {response.status_code}")
            return None

    except requests.Timeout:
        print("Error: Request timed out.")
        return None

if __name__ == "__main__":
    # Replace 'YOUR_SPECIFIC_URL' with the actual URLs of the pages containing the specific data
    urls = [
        'https://www.statistics.gov.rw/publication/gross-domestic-product',
        'https://www.statistics.gov.rw/publication/consumer-price-index',
        'https://www.statistics.gov.rw/publication/life-expectancy-birth',
        'https://www.statistics.gov.rw/publication/size-resident-population'
    ]

    # List to store results for each URL
    all_data = []

    for url in urls:
        # Scrape specific data and append to the list
        specific_data = scrape_specific_data(url, timeout=5)
        if specific_data:
            all_data.append(specific_data)

    # Save the accumulated data to a single JSON file
    with open('exerciseB/fastapi/general_stats.json', 'w') as json_file:
        json.dump(all_data, json_file, indent=2)

    print(f"Data for all URLs saved to 'general_stats.json'")