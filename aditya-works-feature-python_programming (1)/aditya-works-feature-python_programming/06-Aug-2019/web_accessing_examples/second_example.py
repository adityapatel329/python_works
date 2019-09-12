import matplotlib.pyplot as plt
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.google.com/'
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
title = soup.title
print(title)
text = soup.get_text()
print(text)
soup.find_all('a')
all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
rows = soup.find_all("tr")
print(type(rows))
for row in rows:
    row_td = row.find_all('td')
print(row_td)

str_cells = str(row_td)
print(str_cells)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)
