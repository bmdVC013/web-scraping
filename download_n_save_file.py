#! python3
"""
Complete process for downloading and saving a file:
	1. Call requests.get() to download the file.
	2. Call open() with 'wb' to create a new file in write binary mode.
	3. Loop over the Response object's iter_content() method.
	4. Call write() on each iteration to write the content to the file.
	5. Call close() to close the file.
"""

import requests
# get file from url
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
# check a bad download occur
try:
	res.raise_for_status()
except Exception as error:
	print(error)
# open file with write binary mode
playFile = open('RomeoAndJuliet.txt', 'wb')
# write file
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close()