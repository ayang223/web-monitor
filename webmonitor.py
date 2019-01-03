import requests
import json
import time
import smtplib
from bs4 import BeautifulSoup
from pushbullet import PushBullet

token = ""
p = PushBullet(token)
device = p.devices[0]
item = ""

while True:
	url = ""
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.text, 'lxml')

	if str(soup).lower().find(item.lower()) <1:
		time.sleep(30) #sleep 30s
		continue

	else:
		device.push_note("title", "body")
		break
