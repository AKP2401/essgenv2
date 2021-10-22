# Import Module
from bs4 import BeautifulSoup
import requests

# Website URL
URL = 'https://www.geeksforgeeks.org/data-structures/'

# Page content from Website URL
page = requests.get(URL)

# Function to remove tags
def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    para = soup.find