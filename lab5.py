import requests
import streamlit as st

# Function to get the weather data for a location
def get_current_weather(location, API_key):
    if "," in location:
        location = location.split(",")[0].strip()

    # API URL for OpenWeatherMap
    urlbase = "https://api.openweathermap.org/data/2.5/"
    urlweather = f"weather?q={location}&appid={API_key}&units=metric"  # Using 'metric' to get Celsius
    url = urlbase + urlweather

    # Make the API request
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return {"error": "Unable to fetch weather data. Please check your city name or API key."}

    # Extract relevant weather data
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Add logic for clothing suggestions based on temperature
    if temp > 25:
        clothing_suggestion = "It's warm. Wear light clothes like t-shirts and shorts."
    elif 15 <= temp <= 25:
        clothing_suggestion = "It's moderate. A light jacket or sweater would be good."
    else:
        clothing_suggestion = "It's cold. You should wear warm clothes like jackets and scarves."

    # Picnic suggestion based on weather conditions
    if "rain" in weather_desc.lower() or wind_speed > 10:
        picnic_advice = "It might not be a good day for a picnic due to the weather conditions."
    else:
        picnic_advice = "It's a great day for a picnic!"

    # Return the extracted data and suggestions
    return {
        "location": location,
        "temperature": round(temp, 2),
        "feels_like": round(feels_like, 2),
        "weather_description": weather_desc,
        "humidity": round(humidity, 2),
        "wind_speed": round(wind_speed, 2),
        "clothing_suggestion": clothing_suggestion,
        "picnic_advice": picnic_advice
    }

# Add this function to the main Streamlit Lab app as a new page
st.title("Weather Information & Advice")
location_input = st.text_input("Enter a city name:")
if location_input:
    # Ensure the API key is stored in Streamlit secrets
    API_key = st.secrets["OPENWEATHER_API_KEY"]

    # Get the weather data
    weather_info = get_current_weather(location_input, API_key)

    # Display the weather information and suggestions
    if "error" in weather_info:
        st.error(weather_info["error"])
    else:
        st.write(f"### Weather in {weather_info['location']}:")
        st.write(f"**Temperature:** {weather_info['temperature']}°C (Feels like: {weather_info['feels_like']}°C)")
        st.write(f"**Weather:** {weather_info['weather_description']}")
        st.write(f"**Humidity:** {weather_info['humidity']}%")
        st.write(f"**Wind Speed:** {weather_info['wind_speed']} m/s")
        st.write(f"### Clothing Suggestion: {weather_info['clothing_suggestion']}")
        st.write(f"### Picnic Advice: {weather_info['picnic_advice']}")
