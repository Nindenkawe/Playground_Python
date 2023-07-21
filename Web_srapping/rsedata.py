""" 
import requests
from bs4 import BeautifulSoup
import pandas as pd
#grab stat atribute data from the site
def get_info():
    url = "https://www.statistics.gov.rw/"
    results = requests.get(url)
    doc = BeautifulSoup(results.content, 'html5lib')
    table = doc.find('div', attrs = {'class':'figure-value'})
    return(table.prettify()) """


