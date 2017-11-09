"""#! /usr/bin/python"""
import urllib


img_data = urllib.urlopen('http://www.isro.gov.in/sites/default/files/galleries/%E0%A4%AA%E0%A5%80.%E0%A4%8F%E0%A4%B8.%E0%A4%8F%E0%A4%B2.%E0%A4%B5%E0%A5%80.-%E0%A4%B8%E0%A5%8034%20%E0%A4%97%E0%A5%88%E0%A4%B2%E0%A4%B0%E0%A5%80%20/pslv-c34takeoff-view7.jpg')


file_handle1 = open('cartosat2.jpg','w')

while True:
	buffer = img_data.read(100000)
	if len(buffer)<1:
		break
	file_handle1.write(buffer)
	

file_handle1.close()

