import requests,re
from bs4 import BeautifulSoup

# Get the data
data = requests.get('http://www.mesghal.com')

# Load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for td and putting into a list
data_l = []
for tr in soup.find_all('tr'):
    data_l.append(tr.text)

# chopping dollar section into small pieces
data_usd = data_l[-13]
data_re = re.compile(r'\w+')
data_pieces = data_re.findall(data_usd)

# taking last piece as dollar price
print(data_pieces[-1])

