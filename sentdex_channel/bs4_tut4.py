#! python3
# bs4_tut4.py - Scraping Dynamic Javascript Text.

import bs4 as bs
import urllib.request

# Grab source link.
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
# Create a BeautifulSoup object.
soup = bs.BeautifulSoup(source, 'lxml')

# Grab information from 'p' tag within 'jstest' class.
js_test = soup.find('p', class_='jstest')
print(js_test.text) # ~> Wrong answer !!!

# Beautiful Soup doesn't mimic a client. Javascript is code that runs on the client. 
# Let jump in PyQt4.
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

class Client(QWebPage):

	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
        
url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)

# Just in case you wanted to make use of dryscrape.
import dryscrape

sess = dryscrape.Session()
sess.visit('https://pythonprogramming.net/parsememcparseface/')
source = sess.body()

soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)