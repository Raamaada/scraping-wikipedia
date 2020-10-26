import requests
from bs4 import BeautifulSoup

wikipage = requests.get("https://id.wikipedia.org/wiki/Provinsi_di_Indonesia").text
soup = BeautifulSoup(wikipage)
table1 = soup.findAll('tbody')[1]
print(table1)

rows = table1.find_all('tr')

data = []

for row in rows:
    cols = row.find_all('td')
    cols = [nama_provinsi.text.strip() for nama_provinsi in cols]
    data.append([nama_provinsi for nama_provinsi in cols if nama_provinsi])

print(data)