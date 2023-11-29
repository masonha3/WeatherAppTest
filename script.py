import requests
import json
from tkinter import *
from datetime import datetime

# Initialize Window
root = Tk()
root.geometry("400x400") # size of the window by default
root.resizable(0, 0) # to make the window size fixed
root.title("Weather App")

# Create a function to display weather
def show_weather():
    # Enter your API key, copied from the OpenWeatherMap dashboard
    api_key = "your_api_key_here"

    # Get city name from user from the input field
    city_name = city_value.get()

    # API url
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    # Get the response from fetched url
    response = requests.get(weather_url)

    # Changing response from json to python readable
    weather_info = response.json()

    # Clear the text field for every new output
    tfield.delete("1.0", "end")

    # As per API documentation, if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin

        # Storing the fetched values of weather of a city
        temp = int(weather_info['main']['temp'] - kelvin) # converting default kelvin value to Celsius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = datetime.fromtimestamp(sunrise + timezone).strftime('%I:%M:%S %p')
        sunset_time = datetime.fromtimestamp(sunset + timezone).strftime('%I:%M:%S %p')

        # Assigning Values to our weather variable, to display as output
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    # Inserting the weather information into the text field
    tfield.insert(END, weather)

# Create a label for the input field
city_label = Label(root, text="Enter City Name: ", font=("calibri", 10, "bold"))
city_label.pack(pady=10)

# Create an input field for the user to enter the city name
city_value = StringVar()
city_entry = Entry(root, textvariable=city_value, font=("calibri", 10, "normal"), width=30)
city_entry.pack(pady=5)

# Create a button to fetch the weather information
btn = Button(root, text="Get Weather", font=("calibri", 10, "bold"), command=show_weather)
btn.pack(pady=10)

# Create a text field to display the weather information
tfield = Text(root, height=10, width=50, font=("calibri", 10, "normal"))
tfield.pack(pady=10)

# Run the main loop
root.mainloop()
