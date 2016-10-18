GroveWeatherPi Libraries and Example for Raspberry Pi Weather Station

Supports SwitchDoc Labs WeatherRack WeatherBoard (WeatherPiArduino V2 and above)


September 9, 2016 - Added WeatherUnderground Support - see Blog article on www.switchdoc.com for instructions.   The summary of the instructions are:

1) sign up for a personal weather station on weatherunderground.com

2) Get your station name and key and put them in your config.py file, and then setting the WeatherUnderground_Present to True

-----------
setup your configuration variables in config.py!
-----------

--------
Add SQL instructions
----------

Use phpmyadmin or sql command lines to add the included SQL file to your MySQL databases.

example:   mysql -u root -p < WeatherPiStructure.sql

user:  root
password: password

Obviously with these credentials, don't connect port 3306 to the Internet.   Change them if you aren't sure.

NOTE:

If you have a WXLink wireless transmitter installed, the software assumes you have connected your AM2315 outdoor temp/humidity sensor to the WXLink.  If you put another AM2315 on your local system, it will use those values instead of the WXLink values

----------

----------
