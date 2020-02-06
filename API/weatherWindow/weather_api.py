import requests
import json

class weather():
    def __init__(self, city=''):
        myCity = city + ',my'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        self.params = {'APPID': '5a4b158888af8fa4e3577bb66dda5db9', 'q': myCity, 'units': 'metric'}
        self.response = requests.get(url, params=self.params)
        self.weather_json = self.response.json()
        self.weatherIcon = self.weather_json['weather'][0]['icon']

    def format_response(self, weather_json):
        try:
            city = weather_json['name']
            conditions = weather_json['weather'][0]['description']
            temp = weather_json['main']['temp']
            final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (city, conditions, temp)
        except:
            final_str = """There was a problem 
retrieving that information"""
            # final_str = 'hello'
        return final_str

# weather = weather('gua musang')
# print(weather.format_response(weather.weather_json), weather.weatherIcon)

