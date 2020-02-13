import requests
from bs4 import BeautifulSoup

def getUrl(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

# Create for loop to print out all artists' names
    for artist_name in artist_name_list_items:
        print(artist_name.prettify())

if __name__ == "__main__":
    import sys
    getUrl(str(sys.argv[1]))

# https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm