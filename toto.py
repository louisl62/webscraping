#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests # requete (ex : 200)

# récup page html via url
page = requests.get("https://illya3rei.alwaysdata.net/monSite/debian.html")
# pour concaténer la page correctement
soup = BeautifulSoup(page.content, 'html.parser')

print(page.content)
# print(soup.prettify())
