# raspweather
Raspberry Pi 3 and Sensehat Weather Station with Python and Noir Camera

## Installation
Linux: Run this in terminal on your RP3
sudo apt update
sudo apt upgrade
sudo apt install sense_hat
download this repository via git or web and make a local directory for it
sudo reboot

Go to https://www.wunderground.com/

Get an account

Click on my profile on the top right

There should be a section to view weather stations

Add a weather station, you should get an ID and a password

Download project and put in folder

Add your ID and PASSWORD into main.py

Navigate to folder containing the project and run with 'python3 main.py' via shell/cmd whatever

See http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol for information on uploading data, URL construction, etc

## Usage
TODO: Write usage instructions

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## TODO
1. Add webcam support
2. Add sql support
3. Add more LED functionality
4. Add rain and wind sensor support
5. Calibrate temp sensor in a better fashion
6. Make web interface
7. Obtain/make some sort of weatherproof box for mounting project outdoors
8. Readme updates and better installation instructions
9. Separate file for credentials


Feel free to help

## History
I got bored and ordered parts on 10/16/17. The rest will be written here. 

## Credits
OG - MattyMo

## License
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
