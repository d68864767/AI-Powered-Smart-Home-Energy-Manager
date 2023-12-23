```python
# data_collection.py

import requests
import time
from config import DEVICE_DETAILS, WEATHER_API_KEY

# Function to collect data from IoT devices
def collect_device_data(device):
    ip = device['ip']
    port = device['port']
    url = f"http://{ip}:{port}/data"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error occurred while fetching data from device: {e}")
        return None

# Function to collect weather data
def collect_weather_data():
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=YOUR_LOCATION"

    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error occurred while fetching weather data: {e}")
        return None

# Main function to collect all data
def collect_data():
    device_data = {}
    for device_name, device_details in DEVICE_DETAILS.items():
        device_data[device_name] = collect_device_data(device_details)

    weather_data = collect_weather_data()

    return device_data, weather_data

if __name__ == "__main__":
    while True:
        device_data, weather_data = collect_data()
        print(f"Device Data: {device_data}")
        print(f"Weather Data: {weather_data}")

        # Sleep for a while before collecting data again
        time.sleep(60)
```
