# City Weather API

A simple Python Flask API that provides current weather information for a user-specified city. This project currently fetches data from the Open-Meteo API.

## Features (Current)

* Get current weather details (temperature, wind speed, description) for a specific city.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* Python 3.7+ installed
* `pip` (Python package installer) installed
* A virtual environment tool (like `venv`, which comes with Python 3) is recommended.

## Setup and Installation

To get this API running locally, follow these steps:

1.  **Clone the repository (if it's on GitHub):**
    ```bash
    git clone <your-repository-url>
    cd <your-project-directory-name>
    ```
    If you don't have it on GitHub yet, just navigate to your project directory.

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.
    ```bash
    # Create a virtual environment (e.g., named 'venv')
    python -m venv venv
    ```
    Activate the virtual environment:
    * **Windows (Command Prompt/PowerShell):**
        ```bash
        venv\Scripts\activate
        ```
        (For PowerShell, if you encounter issues, you might need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first.)
    * **macOS/Linux (bash/zsh):**
        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    With your virtual environment activated, install the required Python packages:
    ```bash
    pip install Flask requests
    ```
    *(Optional: If you have a `requirements.txt` file, you can use `pip install -r requirements.txt`)*

## Running the API

1.  Ensure your virtual environment is activated.
2.  Navigate to the project directory in your terminal.
3.  Run the Flask application:
    ```bash
    python main.py
    ```
    You should see output indicating the server is running, typically on `http://127.0.0.1:5000/` or `http://0.0.0.0:5000/`.

## API Endpoint (Current)

### Get Weather for a Specific City

* **URL:** `/weather/<city_name>`
* **Method:** `GET`
* **Description:** Retrieves the current weather information for the specified city. Replace `<city_name>` in the URL with the actual name of the city (e.g., `/weather/london`).
* **Example Request:**
    ```
    GET http://localhost:5000/weather/paris
    ```
* **Success Response (200 OK):**
    The API will return a JSON object with weather details. The exact structure will depend on your implementation, but here's a possible example:
    ```json
    {
      "city": "Paris",
      "country": "FR",
      "latitude": 48.8567,
      "longitude": 2.3522,
      "weather": {
        "temperature_celsius": 18.5,
        "wind_speed_kmh": 12.0,
        "weather_code": 3,
        "description": "Partly cloudy",
        "is_day": true,
        "time": "2025-06-03T10:00"
      }
    }
    ```
* **Error Response (e.g., 404 Not Found):**
    If the city is not found or weather data cannot be retrieved:
    ```json
    {
      "error": "Could not find coordinates for city: NonExistentCity"
    }
    ```
    or
    ```json
    {
      "error": "Weather data not found for Paris"
    }
    ```

## How to Test

You can test the API endpoint using:

* Your web browser (by typing the URL directly)
* API testing tools like Postman, Hoppscotch, or Insomnia.
* Command-line tools like `curl`. Example:
    ```bash
    curl http://localhost:5000/weather/berlin
    ```

## Future Enhancements (Planned)

* Add an endpoint to get weather for a random location.
* Add an endpoint to get an estimated global average weather.
* Implement more robust error handling.
* Add more weather details to the response.

## Contributing

Contributions are welcome! If you have suggestions or want to improve the API, please feel free to fork the repository and submit a pull request, or open an issue.
(If your project is not yet on a platform like GitHub, you can remove or modify this section.)

---

Made with Python and Flask.