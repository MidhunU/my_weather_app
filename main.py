from flask import Flask, jsonify, request
import requests
import random

app = Flask(__name__)

def get_cordinates(city_name):
    try:
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        response = requests.get(geocode_url, timeout = 10)
        response.raise_for_status()
        data = response.json()

        if data.get("results"):
            location = data["results"][0]
            return location.get("latitude"), location.get("longitude"), location.get("name", city_name), location.get("country_code", "")
        
    except requests.exceptions.RequestException as e:
        print(f"Error geocoding {city_name}: {e}")

    except (KeyError, IndexError) as e:
        print(f"Error parsing geocoding response for {city_name}: {e}")

    return None, None, city_name, None

def get_weather_data(latitude, longitude):
    if latitude is None or longitude is None:
        return None
    try:
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=celsius&wind_speed_unit=kmh&precipitation_unit=mm"
        response = requests.get(weather_url, timeout=10)
        response.raise_for_status()
        data=response.json()

        if data.get("current_weather"):
            current = data["current_weather"]
            weather_code = current.get("weather_code", 0)
            descripton = "Unknown"
            if weather_code ==0: description = "Clear Sky"
            elif weather_code in [1,2,3]: description = "Mainly clear, partly cloudy, and overcast"
            elif weather_code in [51, 52, 53]: description = "Drizzle (light, moderate, heavy)"
            elif weather_code in [45, 48]: description = "Fog and depositing rime fog"
            elif weather_code in [56, 57]: description = "Freezing Drizzle: Light and dense intensity"
            elif weather_code in [61, 63, 65]: description = "Rain: Slight, moderate and heavy intensity"
            elif weather_code in [66, 67]: description = "Freezing Rain: Light and heavy intensity"
            elif weather_code in [71, 73, 75]: description = "Snow fall: Slight, moderate, and heavy intensity"
            elif weather_code == 77: description = "Snow grains"
            elif weather_code in [80, 81, 82]: description = "Rain showers: Slight, moderate, and violent"
            elif weather_code in [85, 86]: description = "Snow showers slight and heavy"
            elif weather_code == 95: description = "Thunderstorm: Slight or moderate"
            elif weather_code in [96, 99]: description = "Thunderstorm with slight and heavy hail"

            return{
                "temperature": current.get("temperature"),
                "weather_code": weather_code,
                "description": description,
                "time": current.get("time")
            }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather for {latitude}, {longitude}: {e}")
    except KeyError as e:
        print(f"Error parsing weather data")
    return None 

@app.route("/weather/<city_name>", methods=['GET'])
def weather_by_city(city_name):
    lat, lon, official_name, country = get_cordinates(city_name)

    if lat is None and lon is None:
        return jsonify({"error": f"could not find the cordinates of the city: {city_name}"}), 404
    
    weather_data = get_weather_data(lat, lon)
    if weather_data:
        return jsonify({
            "city": official_name,
            "country": country,
            "latitude": lat,
            "longitude": lon,
            "weather": weather_data

        })
    return jsonify({"Error: could not find the weather data for {official_name}"}), 404

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)