from bs4 import BeautifulSoup
import requests, bs4
import re
# page_link='http://Html_file.html'
# page_response = requests.get(page_link,timeout=5)
# page_content = bs4.BeautifulSoup(open("C:\Html_file.html"), "html.parser")  # lxml is specification for the parser

# prices= page_content.find_all(class_='main_price')

# prices=page_content.find_all('div',attrs={'class':'main_price'})
url = "C:/Html_file.html"
page = open(url)
soup = BeautifulSoup(page.read())
prices= soup.find_all(class_='main_price')
#print(soup)
regex='Price:(.*)\$'
pri=re.findall(regex,page)
# cities = soup.find_all('div',attrs={'class':'main_price'})
print(pri)
print(prices)
#print(page_content)