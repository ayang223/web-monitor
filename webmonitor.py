import requests
import json
import time
import smtplib
from bs4 import BeautifulSoup
from pushbullet.pushbullet import PushBullet

token = "pushbullet token"
p = PushBullet(token)
devices = p.getDevices()
item = "what to monitor for"

while True:
	url = ""
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.text, 'lxml')

	if str(soup).lower().find(item.lower()) <1:
		time.sleep(30) #sleep 30s
		continue

	else:
		p.pushNote(devices[0]["iden"], 'Item found', item)
		break
