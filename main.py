from bs4 import BeautifulSoup
import requests # requete (ex : 200)

# récup page html via url
page = requests.get("https://www.data.gouv.fr/")
# pour concaténer la page correctement
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())
print(soup.find_all('p')[0].get_text())