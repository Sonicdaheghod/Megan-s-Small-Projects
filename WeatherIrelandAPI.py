# Significance of this project: To better understand the intricacies of an API and its applications
# reference video: Intermediate Python for Non-Programmers by Nick Walters on Linkedin Learning
# I will practice using API using weather data from Ireland


##API key: 6cd640b6d94034814baef94446b8b3ff

#Plugging in API, lat and longtitude for Ireland using API key to get data 
#https://api.openweathermap.org/data/2.5/weather?lat=53.1424&lon=7.6921&appid=6cd640b6d94034814baef94446b8b3ff


#importing package
import requests
# first we have to install requests using "pip install requests"

output = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=53.1424&lon=7.6921&appid=6cd640b6d94034814baef94446b8b3ff")

#this will print out the JSON data about Ireland as well as its source code(200 = work well, 404 = error, etc.)
print(output.content)
