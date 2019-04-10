#! python3

import requests, bs4
import warnings
warnings.filterwarnings("ignore")

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())

elems = exampleSoup.select('#author')
print("Type: ", type(elems))
print("Length: ", len(elems))
print("Type elems[0]: ", type(elems[0]))
print("Get text elems[0]: ",elems[0].getText())
print("String: ", str(elems[0]))
print("Attributions: ", elems[0].attrs)
print('*'*13)
print()

pElems = exampleSoup.select('p')
print("String pElems[0]: ", str(pElems[0]))
print("Get text pElems[0]: ", pElems[0].getText())
print()
print("String pElems[1]: ", str(pElems[1]))
print("Get text pElems[1]: ", pElems[1].getText())
print()
print("String pElems[2]: ", str(pElems[2]))
print("Get text pElems[2]: ", pElems[2].getText())
print('*'*13)
print()

spanElem = exampleSoup.select('span')[0]
print("String spanElem[0]: ", str(spanElem))
print("Get value from tag 'id': ", spanElem.get('id'))
print("Non-exists: ", spanElem.get('some_nonexistent_addr') == None)
print("Attributions: ", spanElem.attrs)
print('*'*13)
print()