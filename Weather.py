def weather_app():
    weather_data = {
        "new york": "☀️ Sunny, 25°C",
        "london": "🌧️ Rainy, 18°C",
        "tokyo": "⛅ Cloudy, 22°C",
        "paris": "🌦️ Light showers, 20°C",
        "mumbai": "☀️ Hot, 32°C"
    }

    print("🌤️ Simple Weather App")
    while True:
        city = input("\nEnter a city name (or 'q' to quit): ").lower()
        if city == "q":
            print("👋 Thanks for checking the weather!")
            break
        if city in weather_data:
            print(f"Weather in {city.title()}: {weather_data[city]}")
        else:
            print("⚠️ Sorry, weather data not available for this city.")

weather_app()
