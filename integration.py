```python
# integration.py

import requests
import json
from config import DEVICE_DETAILS
from data_collection import collect_data
from model import train_model, save_model
from data_analysis import preprocess_data

# Function to send control signals to IoT devices
def send_control_signal(device, control_signal):
    ip = device['ip']
    port = device['port']
    url = f"http://{ip}:{port}/control"

    try:
        response = requests.post(url, data=json.dumps(control_signal))
        if response.status_code == 200:
            print(f"Control signal sent to {device['type']}")
        else:
            print(f"Failed to send control signal to {device['type']}")
    except Exception as e:
        print(f"Error occurred while sending control signal to device: {e}")

# Function to generate control signals based on the model's prediction
def generate_control_signals(model, device_data, weather_data):
    df = preprocess_data(device_data, weather_data)
    prediction = model.predict(df)

    control_signals = {}
    for device in DEVICE_DETAILS.keys():
        if prediction > df['energy_usage'].mean():
            control_signals[device] = 'off'
        else:
            control_signals[device] = 'on'

    return control_signals

# Main function to integrate all parts
def main():
    device_data, weather_data = collect_data()
    df = preprocess_data(device_data, weather_data)
    model = train_model(df)
    save_model(model, 'model.pkl')

    control_signals = generate_control_signals(model, device_data, weather_data)

    for device_name, control_signal in control_signals.items():
        send_control_signal(DEVICE_DETAILS[device_name], control_signal)

if __name__ == "__main__":
    main()
```
