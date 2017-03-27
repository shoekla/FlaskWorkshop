try:
	from flask import Flask
	print "Flask Part 1"
	from flask import request
	print "Flask Part 2"
	from flask import render_template
	print "Flask Part 3"
	from flask import redirect
	print "Flask Installation PASSED!"
	import time
	print "TIME Installation PASSED!"
	import requests
	print "REQUESTS Installation PASSED!"
	from bs4 import BeautifulSoup
	print "bs4 Installation PASSED!"
	from urllib2 import urlopen
	print "urllib2 Installation PASSED!"
	print "\n\nAll Good!!!!!!!!\n"
except Exception as e:
	print str(e)
	print "\nTEST FAILED CALL ORGANIZER"