#! python3
# bs4_tut2.py - Navigation with Beautiful Soup 4.

import bs4 as bs
import urllib.request

# Grab source link.
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# Create a BeautifulSoup object.
soup = bs.BeautifulSoup(source, 'lxml')

# Specify a new Beautiful Soup object.
nav = soup.nav

# Grab the links from just the nav bar.
for url in nav.find_all('a'):
	print(url.get('href'))

# Get the body section, then grab the .text from there.
body = soup.body
for paragraph in body.find_all('p'):
	print(paragraph.text)

# Grab information from a specific tag with a specific class.
for div in soup.find_all('div', class_ = 'body'):
	print(div.text)