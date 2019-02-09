# Grabbing the Weather
A program that prompts for a city name and returns the current temperature for the city.

## Getting Started
### Prerequisites
API Keys
* [Open Weather Map API](http://openweathermap.org/appid)

Install requests package for API requests 
```pip install requests```

Create environment variables for the API keys
* ```OWM_KEY= <Open Weather Map API key>```
### Running
Run weather.py and enter city name.

Example
```
Where are you? Grinnell IA 
Chicago weather:
20.0 degrees Fahrenheit 
```

## Testing
Run tests.py

* ```test_get_city_temp``` - Tests getting temperature data from the Open Weather API response.
* ```test_city_not_found``` - Tests that the program handles invalid city names.