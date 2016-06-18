#=======================
# Cteated by Alex
#=======================


#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import os
import re
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

count = 0

def has_nickname(tag):
	return tag.has_attr('data-nickname')

def catch_data(data,x):
	soup = BeautifulSoup(data)

	m = soup.findAll(has_nickname)
	file = open('final_data{}.txt'.format(x/20),'a')
	for i in m:
		inner_soup = BeautifulSoup(str(i))

		dd = inner_soup.findAll('dd')
		star = inner_soup.findAll(class_=re.compile('star.*'))
		u_name = inner_soup.findAll(class_='u-name')

		for ddd in dd:
			try:
				tmp = str(ddd)[4:-5].encode('gb2312').strip()
				if '<' in tmp:
					continue
				# print 'ddd'+ tmp
				file.write(tmp)
				file.write(',')
			except Exception as e:
				print str(e)+'---------in'+str(x)

		for sss in star:
			tmp = str(sss)[20:-9].strip()
			if '<' in tmp:
				continue
			# print 'sss'+ tmp
			file.write(tmp)
			file.write(',')
		tmp = str(u_name[0])[21:-10].strip()
		if '<' in tmp:
			continue
		# print 'uuu'+ tmp
		file.write(tmp)
		file.write(',')
		file.write('\n')
	file.close()


iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver



for y in xrange(0,19):
	driver = webdriver.Ie(iedriver)
	#store in some small files
	for x in xrange(20*y,20*(y+1)):
		for i in xrange(0,100):
			print "http://club.jd.com/review/1298438602-1-{}-0.html".format(x)
			driver.get("http://club.jd.com/review/1298438602-1-{}-0.html".format(x))
			html = driver.page_source
			soup = BeautifulSoup(html)
			title = soup.findAll('title')
			print str(title[0]).strip()
			if '季德胜' not in str(title[0]).strip():
				print str(title)
				continue
			else:
				catch_data(html,x)
				break
	driver.quit()