# configuration file - contains customization for exact system
# JCS 11/8/2013
mailUser = "skip@angerbunny.net"
mailPassword = "minter73"
notifyAddress ="skip@zerosquadron.com"
fromAddress = "weather@angerbunny.net"

# MySQL Logging and Password Information
enable_MySQL_Logging = False
MySQL_Database = "pi_weather"
MySQL_Username = "pi_weather"
MySQL_Password = "pipi1138"

# modify this IP to enable WLAN operating detection  - search for WLAN_check in GroveWeatherPi.py
enable_WLAN_Detection = True
PingableRouterAddress = "10.0.0.1"

# WeatherUnderground Station
WeatherUnderground_Present = False
WeatherUnderground_StationID = "KWXXXXX"
WeatherUnderground_StationKey = "YYYYYYY"

# for barometeric pressure - needed to calculate sealevel equivalent - set your weatherstation elevation here
BMP280_Altitude_Meters = 40.0

# device present global variables
Lightning_Mode = False
SolarPower_Mode = False

TCA9545_I2CMux_Present = False
SunAirPlus_Present = False
AS3935_Present = False
DS3231_Present = False
BMP280_Present = True
FRAM_Present = True
HTU21DF_Present = False
AM2315_Present = True
ADS1015_Present = False
ADS1115_Present = False
OLED_Present = False
WXLink_Present = False

# if the WXLink has stopped transmitting, == False
WXLink_Data_Fresh = False
WXLInk_LastMessageID = 0
