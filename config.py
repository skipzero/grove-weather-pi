
#
#
# configuration file - contains customization for exact system
# JCS 11/8/2013
#

# it is a good idea to copy this file into a file called "conflocal.py" and edit that instead of this one.  This file is wiped out if you update GroveWeatherPi.

mailUser = "bfalcon510@gmail.com"
mailPassword = "minterFalcon!138"

notifyAddress ="bfalcon510+notification@gmail.com"

fromAddress = "bfalcon510@gmail.com"

# textnotifyAddress = "yourphonenumber@yourprovider"

#MySQL Logging and Password Information

enable_MySQL_Logging = True
MySQL_Password = "minter73"

# modify this IP to enable WLAN operating detection  - search for WLAN_check in GroveWeatherPi.py
enable_WLAN_Detection = True
PingableRouterAddress = "10.0.0.1"

# WeatherUnderground Station

WeatherUnderground_Present = False
WeatherUnderground_StationID = "KWXXXXX"
WeatherUnderground_StationKey = "YYYYYYY"

############
# Blynk configuration
############

USEBLYNK = True
BLYNK_AUTH = '8150b6c3073a4912a95a2194b750a9ef'
BLYNK_URL = 'http://blynk-cloud.com/'



# for barometeric pressure - needed to calculate sealevel equivalent - set your weatherstation elevation here

BMP280_Altitude_Meters = 40.0

# device present global variables

Lightning_Mode = False
SolarPower_Mode = False

TCA9545_I2CMux_Present = True
SunAirPlus_Present = False

AS3935_Present = True
DS3231_Present = True
BMP280_Present = True
FRAM_Present = True
HTU21DF_Present = True
HDC1080_Present = True
AM2315_Present = True
ADS1015_Present = False
ADS1115_Present = True
OLED_Present = True
OLED_Originally_Present = True
WXLink_Present = False
Sunlight_Preset = False

# set Sunlight High Gain (indoors - 1) or Low Gain (outdoors - 0)
Sunlight_Gain = 1


# if the WXLink has stopped transmitting, == False
WXLink_Data_Fresh = False
WXLInk_LastMessageID = 0
