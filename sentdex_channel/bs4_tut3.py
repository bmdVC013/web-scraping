#! python3
# bs4_tut3.py - Parsing tables and XML with Beautiful Soup 4.

import bs4 as bs
import urllib.request

# Grab source link.
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# Create a BeautifulSoup object.
soup = bs.BeautifulSoup(source, 'lxml')

# This page just has one table, so we can get away with doing.
table = soup.table
# OR
#table = soup.find('table')

# Find the table rows within the table.
table_rows = table.find_all('tr')

# Iterate through the rows, find the 'td' tags, and then print out each
# of table data tags.
for tr in table_rows:
	td = tr.find_all('td')
	row = [i.text for i in td]
	print(row)

# Reading table from url by using pandas.
import pandas as pd 
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
for df in dfs:
	print(df)

# To parse XML.
source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(source, 'xml')

# Grab the uris
for url in soup.find_all('loc'):
	print(url.text)