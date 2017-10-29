from ftplib import FTP
import ftplib
import time
from picamera import PiCamera
import datetime
import os

SERVER_URL = 'webcam.wunderground.com'
USERNAME = ''  #put your ftp username here
PASSWORD = ''  #put your password here

FILENAME ='/home/pi/raspweather/noir/img/image.jpg'


def take_ftp_image():
	'''
	Outputs file with the date and time of the capture
	'''
	camera = PiCamera()
	camera.capture(FILENAME, quality=8)
	camera.close()
	return


while True:
	#take image
	take_ftp_image()

	#connect and upload
	try:
		ftp = FTP(SERVER_URL)
	except ftplib.all_errors as e:
		print('FTP fail -> ', e)

	ftp.login(user=USERNAME, passwd=PASSWORD)
	print(ftp.getwelcome()+'\n')
	ftp.cwd('/')
	ftp.set_pasv(True)

	myfile = open(FILENAME, 'rb')
	ftp.storbinary("STOR " + 'image.jpg', myfile)
	ftp.quit()
	
	myfile.close()
	os.remove(FILENAME)

	print('running: {} \n'.format(datetime.datetime.now()))

	#sleep and take another picture in 300 seconds
	time.sleep(300)