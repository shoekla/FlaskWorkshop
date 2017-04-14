import urllib2
import re
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen

def scrape(url):
	pages = []
	source_code = requests.get(url) #Gets source Code
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	for link in soup.findAll('a'):
		href = str(link.get("href")) #Gets the actual link
		if "bing" not in href and "go.microsoft.com" not in href and "http://www.freebase.com/" not in href:
			if href.startswith("http"):
				if href not in pages:
					pages.append(href)
	return pages

def getSearch(name):
	name = name.replace(" ","+")
	url = "http://www.bing.com/search?q="+name+"&qs=n&form=QBLH&sp=-1&pq="+name+"&sc=9-6&sk=&cvid=ACF31D8DC7A140AC8CF356A0F61E10A1"
	return scrape(url)
def scrapeVideo(url):
	pages = []
	source_code = requests.get(url) #Gets source Code
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text,"html.parser")
	for link in soup.findAll('a'):
		href = str(link.get("href")) #Gets the actual link
		if "bing" not in href and "go.microsoft.com" not in href and "http://www.freebase.com/" not in href:
			if href not in pages:
				pages.append(href)
	return pages
def getVideoSearch(name):
	name = name.replace(" ","+")
	url = "https://www.youtube.com/results?search_query="+name
	arr = scrapeVideo(url)
	results = []
	for i in arr:
		if "/watch" in i:
			if i not in results:
				results.append(i.replace("/watch?v=",""))
	return results









