import requests
from bs4 import BeautifulSoup

# Aşağıdaki kısma url'yi girin
# Enter the URL in the field below
url = ' '

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


title = soup.find('title').get_text()
print(title)


links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
print(links)
