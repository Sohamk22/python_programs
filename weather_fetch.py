
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        main_info = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp = main_info["temp"]
        humidity = main_info["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print(f"Weather in {city}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API key invalid.")

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = 'a2f5cbe8d5a868ef02bfc1b9fbc0f84f'
city = input("Enter city name: ")
get_weather(api_key, city)