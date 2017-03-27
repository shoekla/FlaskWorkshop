import time
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis

def crawl(term):
	try:
		url = turnToSearch(term)
		pages=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			if "microsoft" not in href_test and "facebook" not in href_test and "twitter" not in href_test and "google" not in href_test:
				if href_test.startswith("http"):
					if "bing" not in href_test:
						pages.append(href)
		return deleteDuplicates(pages)


	except:
		print "Error at: "+str(url)



def turnToSearch(text):
	search=text.replace(" ","%20")
	link="http://www.bing.com/search?q="+str(search)+"&qs=n&form=QBRE&pq="+str(search)+"&sc=9-6&sp=-1&sk=&cvid=6585c559beef41f3b942271b982e674a"
	return link

#TEST

a = "purdue hackers"
pages = crawl(a)
for i in pages:
	print i



