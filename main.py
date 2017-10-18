from sense_hat import SenseHat
import time
import subprocess
import requests
import json
from datetime import date
from datetime import datetime

'''
Put your settings here. Get ID and PASSWORD from the Weather Underground Personal Weather Station website. 
See readme for more information
'''
ID = "" #put your personal weather station ID between the quotes
PASSWORD = "" #put your personal weather station password between the quotes
WU_GET_URL = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php" #weather updates URL
'''
The following three variables are used for obtaining local weather, and may be implemented in future versions
of this software using the function get_local_weather
'''
LOCAL_WEATHER_KEY = "" #Weather underground local weather key
STATE = "" #choose a state to get the weather
CITY = "" #choose a city to get the weather

sense = SenseHat()

def get_temp():
	'''read temp in C from sensehat, converts to C, corrects temp for being close to processor, returns 'calibrated' temp'''
	temp_c = sense.get_temperature()
	temp_f = (temp_c * 1.8) + 32
	cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
	cpu_temp = cpu_temp[5:9]
	cpu_temp = float(cpu_temp)
	#using two as the 'scaling factor' is arbitrary and will be updated in the future, right now this gives 'okay' results
	calibrated_temp_c = temp_c - ((cpu_temp-temp_c)/2)
	calibrated_temp_f = (calibrated_temp_c * 1.8) + 32
	return calibrated_temp_f

def get_pressure():
	'''reads press in mb from sensehat, returns press in inches'''
	pressure_mb = sense.get_pressure()  
	pressure_in = pressure_mb * 0.02953
	return pressure_in

def dewpoint_calc(t, h):
	'''calculates dewpoint using temp and humidity'''
	return t - (100 - h)/5

def get_local_weather(l, s, c):
	#inputs: local weather api key from weather underground (l) -  not the same key as the PWS, state (s), and city (c)
	try:
		my_weather = requests.post("http://api.wunderground.com/api/" + l + "/geolookup/conditions/q/" + s + "/" + c + ".json")
	except:
		print("Error - unsuccesful connection")
		return []
	return my_weather.json()      


def pws_upload(humidity, dewpoint, temp, pressure):
	'''uses request to send the data to the weather underground url, payload gets tacked onto WU_GET_URL'''
	payload = {
		'ID' : ID, 
		'PASSWORD': PASSWORD, 
		'dateutc': 'now', #can be changed to system time
		'humidity' : humidity,
		'dewptf' : dewpoint, 
		'tempf' : temp, 
		'baromin' : pressure, 
		'action' : 'updateraw'
		}

	try:
		r = requests.get(WU_GET_URL, params = payload)
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)
	
	#r.text returns success when your get request worked properly, i think
	if len(r.text) == 8:
		print("Station Operable")

	return 

def main():
	
	while True:
		#
		temp = get_temp()
		humidity = sense.get_humidity()
		pressure = get_pressure()
		dewpoint = dewpoint_calc(temp, humidity)

		#send data to weather underground
		pws_upload(humidity, dewpoint, temp, pressure)

		#print data
		print('Time = {}'.format(datetime.now()))
		print('Temperature = {} deg F'.format(temp))
		print('Humidity = {}%'.format(humidity))
		print('Dewpoint = {}'.format(dewpoint))
		print('Pressure = {} mb'.format(pressure))
		print('----------------------------------------------------')
		sense.show_message("{:02.0f}".format(temp), text_colour=[0,0,255])
		time.sleep(10)

main()