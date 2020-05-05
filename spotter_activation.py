#!/usr/bin/python3

#Program to check if spotter activation is expected for Fort Worth
import requests, re, datetime
from bs4 import BeautifulSoup
from notify_run import Notify
notify = Notify()

# Download Page
url = 'https://forecast.weather.gov/product.php?site=NWS&issuedby=FWD&product=HWO'
html_content = requests.get(url).text 

# Parse for Spotter
soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify())

# Find the section by css where text of interest is
location = soup.find('pre', {'class': 'glossaryProduct'})
if location is not None:
	location_text = location.text.strip()
#print(location_text)

#Looks for Spotter activation is expected and returns that line
activation_match = r'(?i)(\W|^)(spotter\sactivation\sis\sexpected|limited\sspotter\sactivation)(\W|$)*([^\n\r]*)'
activation_check = re.search(activation_match, location_text)
if activation_check is not None:
	print(datetime.datetime.now(),activation_check.group(0))
	notify.send(activation_check.group(0), url)
else:
	print("Spotter activation not expected at this time")
