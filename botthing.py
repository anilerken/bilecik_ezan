# source for regex thing: https://stackoverflow.com/a/1376658/5931579

import datetime
import tweepy
import time
import urllib2
import re
import os

auth = tweepy.OAuthHandler('xxxxxxxxxxxx', 'xxxxxxxxxx')
auth.set_access_token('xxxxxxxxxx', 'xxxxxxxxxxxxx')

api = tweepy.API(auth)

times = []

# get the page source code to content
req = urllib2.Request('http://www.namazvaktim.net/xml/gunluk/bilecik/bilecik.xml', headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
content = con.read()

# search and get imsak, put to list
r = re.compile('<imsak>(.*?)</imsak>')
m = r.search(content)
if m:
	imsak = m.group(1)
	times.append(imsak)

# search and get ogle, put to list
r = re.compile('<ogle>(.*?)</ogle>')
m = r.search(content)
if m:
	ogle  = m.group(1)
	times.append(ogle)

# search and get ikindi, put to list
r = re.compile('<ikindi>(.*?)</ikindi>')
m = r.search(content)
if m:
	ikindi  = m.group(1)
	times.append(ikindi)

# search and get aksam, put to list
r = re.compile('<aksam>(.*?)</aksam>')
m = r.search(content)
if m:
	aksam  = m.group(1)
	times.append(aksam)

# search and get yatsi, put to list
r = re.compile('<yatsi>(.*?)</yatsi>')
m = r.search(content)
if m:
	yatsi  = m.group(1)
	times.append(yatsi)

# update status if now is the time
while True:
	now = datetime.datetime.now()
	nowtime = str(now)[11:16]

	if nowtime in times:
		api.update_status('TANRI ULUDUR TANRIIIIIIIIIIII ULUDUR - ' + str(now))
		# wait a minute
		time.sleep(60)
