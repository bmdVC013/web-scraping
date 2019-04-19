#! python3
# bs4_tut1.py - Introduction.

import bs4 as bs 
import urllib.request

# Grab source code.
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# Create a BeautifulSoup object.
soup = bs.BeautifulSoup(sauce,'lxml')

# Title of the page.
print(soup.title)

# Get attribute.
print(soup.title.name)

# Get values.
print(soup.title.string)

# Beginning navigation.
print(soup.title.parent.name)

# Getting specific value.
print(soup.p)

# Grab text.
print(soup.get_text())

# Finding all paragraph tags <p>.
print(soup.find_all('p'))
# Also iterate through them
for paragraph in soup.find_all('p'):
	print(paragraph.string)		# .string produces a NavigableString object
	print(str(paragraph.text))	# .text produces unicode text

# To grab links.
for url in soup.find_all('a'):
	print(url.get('href'))

