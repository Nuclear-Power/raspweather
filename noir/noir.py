from picamera import PiCamera
import time
#from time import sleep
import datetime

def take_still_image():
	'''
	Outputs file with the date and time of the capture
	'''
	camera = PiCamera()
	filename = datetime.datetime.now().time()
	camera.capture('/home/pi/raspweather/noir/img/{}.jpg'.format(filename))
	camera.close()
	return

def record_video(s):
	'''Input of seconds to reoord. Records  video with the noir camera'''
	camera = PiCamera()
	filename = datetime.datetime.now().time()
	camera.start_recording('/home/pi/raspweather/noir/vid/{}.h264'.format(filename), format='h264', resize=(500,400),  quality=25)
	time.sleep(s)
	camera.stop_recording()
	camera.close()
	return

record_video(5)
time.sleep(5)
take_still_image()
