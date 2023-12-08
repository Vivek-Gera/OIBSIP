import requests
import json
def get_weather(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            # Extract weather data
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_condition = data["weather"][0]["description"]

            # Print weather information
            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {weather_condition}")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException:
        print("Failed to connect to the weather service")
    except json.JSONDecodeError:
        print("Failed to parse the weather data")
if __name__ == "__main__":
    api_key = "d40579830861801596191d8069d86bf8"
    location = input("Enter a city or ZIP code: ")
    get_weather(api_key, location)
