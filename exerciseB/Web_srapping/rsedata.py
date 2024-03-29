import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_and_save_data(url, timeout_seconds=5, output_file="exerciseB/fastapi/rse_data.json"):
    try:
        response = requests.get(url, timeout=timeout_seconds, verify=False)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        marquee_tag = soup.find('marquee')

        if marquee_tag:
            result = {}
            for div_tag in marquee_tag.find_all('div'):
                text = div_tag.get_text(strip=True)

                # Use regular expressions to extract name, stock price, and currency
                match = re.search(r'(\w+)\s+(\d+)\s+(\w+)', text)
                if match:
                    name, stock_price, currency = match.groups()
                    result[name] = {"stock_price": stock_price, "currency": currency}

            # Format the data as requested
            formatted_data = [{"name": key, "stock_price": value["stock_price"], "currency": value["currency"]} for key, value in result.items()]
            json_output = {"data": formatted_data}

            # Save the data to a file
            with open(output_file, 'w') as file:
                json.dump(json_output, file)

            print(f"Data saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage:
scrape_and_save_data("https://rse.rw")
