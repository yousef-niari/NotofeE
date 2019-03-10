import requests,re
import xml
from bs4 import BeautifulSoup

# Get the data
data = requests.get('http://www.sanarate.ir/')

# Load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for td and putting into a list
print(soup.prettify())

#----------------------------
data_l = []
for div in soup.find_all('div',{'class':'panel-body'}):
     #values = [td.text for td in tr.find_all('td')]
     data_l.append(div.text)

# chopping dollar section into small pieces
print(len(data_l))
print(data_l)
# data_usd = data_l[-13]
# data_re = re.compile(r'\w+')
# data_pieces = data_re.findall(data_usd)

# taking last piece as dollar price
#print(data_pieces[-1])