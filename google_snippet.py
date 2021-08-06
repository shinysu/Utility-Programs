import requests
from bs4 import BeautifulSoup
import re


def clean_link(link):
    clean = re.search('\/url\?q\=(.*)\&sa', link)
    if clean is None:
        return False
    else:
        return clean.group(1)


def get_snippet(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})
    for r in result_div:
        try:
            link = r.find('a', href=True)
            description = r.find('div', attrs={'class': 's3v9rd'}).get_text()
            link = clean_link(link['href'])
            if clean_link:
                print(description)
                print(link)
                break
        except:
            continue


word = input("Enter the search term: ")
search_query = "define " + word
url = 'https://google.com/search?q=' + search_query
get_snippet(url)
