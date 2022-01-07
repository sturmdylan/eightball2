from bs4.element import TemplateString
import requests
from bs4 import BeautifulSoup 

url = "https://www.wkbn.com/weather/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "")
# print(soup.title)
# temp = soup.find_all('div', class_="")
temp = soup.find_all('div', attrs= {"":"}
     print(temp[0].text)
print()
for div in temp:
    print(div)
print()
# print(soup.prettify())




# print temp
# for items in soup.found_all
    # print(items.get(''))