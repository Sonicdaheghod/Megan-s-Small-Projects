# Significance of this project: To better understand the intricacies of an API and its applications
# reference video: Intermediate Python for Non-Programmers by Nick Walters on Linkedin Learning
# I will practice using API using weather data from Ireland


#JSON validator: reformats JSON data https://jsonlint.com/

##API key: 6cd640b6d94034814baef94446b8b3ff

#Plugging in API, lat and longtitude for Ireland using API key to get data 
#https://api.openweathermap.org/data/2.5/weather?lat=53.1424&lon=7.6921&appid=6cd640b6d94034814baef94446b8b3ff


#importing package
import requests
# first we have to install requests using "pip install requests"
## apply try except 
try:
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?units=metric&lat=53.1424&lon=7.6921&appid=6cd640b6d94034814baef94446b8b3ff")

except:
    print("An error occured.")
#this will print out the JSON data about Ireland as well as its source code(200 = work well, 404 = error, etc.)

output_json = response.json()

#define variables using data from JSON
wind = output_json["wind"]["speed"]

#utilizing variables in print statements
print("The wind speed in Ireland is " + str(wind) + " mph")

#Creating class to have certain information about something specific
class City:
    def __init__(self,name, feels_like, units="metric"):
        self.name = name
        
        self.feels_like= feels_like
        self.units = units
        self.retrieveInfo() #goes through the retrieveInfo function to get its info
    #we need a new function in the class that calls for the API
    def retrieveInfo(self):
        try:
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat=53.1424&lon=7.6921&appid=6cd640b6d94034814baef94446b8b3ff")

        except:
            print("An error occured.")

        output_json = response.json()
        self.wind = output_json["wind"]["speed"]
        self.feels_like = output_json["main"]["feels_like"]
        
        print("The wind speed in Ireland is " + str(wind) + " mph")
        #self helps us access all instances of a specific class

    def weatherDescription(self):
     
        print(f"In Ireland it is {self.feels_like}°C outside.")
        

theCity = City("Strücklingen",7.6921,53.1424)
theCity.weatherDescription()

