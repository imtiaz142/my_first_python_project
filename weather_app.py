
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        print(f"\n🌤 Weather in {city.title()}:\nTemperature: {temp}°C\nCondition: {condition}")
    else:
        print(f"\n❌ Error: {data.get('message', 'Could not fetch weather data')}")

# --- MAIN PROGRAM ---
print("🛰 Simple Weather App")
api_key = "a42616ef15363a4248917e9834e6ddd9"  # <== Use the new key here

city_name = input("Enter city name: ")
get_weather(city_name, api_key)
