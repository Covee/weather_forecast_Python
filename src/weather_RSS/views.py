from django.shortcuts import render

import urllib.request
from django.http import HttpResponse

from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml

import feedparser


def weather(request):
	url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1114052000"
	feed = feedparser.parse(url)

	bring = urllib.request.urlopen(url)
	soup = BeautifulSoup(bring.read(), 'lxml')

	data = soup.findAll('data', attrs={'seq':'0'})
	where_data 	= soup.find('category')
	where 	= where_data.text
	date 	= feed.feed.published

	weather = data[0].find('wfkor').text
	temp	= data[0].find('temp').text
	hum 	= data[0].find('reh').text
	rain 	= data[0].find('pop').text
	wind_d 	= data[0].find('wdkor').text
	wind_s 	= data[0].find('ws').text


	return render(request, 'weather_RSS/weather.html', {
			"weather": weather,
			"where": where,
			"date": date,
			"temp": temp,
			"hum": hum,
			"rain": rain,
			"wind_d": wind_d,
			"wind_s": wind_s,
			
		})

