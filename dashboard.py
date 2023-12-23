```python
# dashboard.py

from flask import Flask, render_template, jsonify
from data_collection import collect_data
from model import train_model
from data_analysis import preprocess_data
from integration import generate_control_signals
from config import DEVICE_DETAILS

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    device_data, weather_data = collect_data()
    df = preprocess_data(device_data, weather_data)
    model = train_model(df)
    control_signals = generate_control_signals(model, device_data, weather_data)

    data = {
        'device_data': device_data,
        'weather_data': weather_data,
        'control_signals': control_signals
    }

    return jsonify(data)

@app.route('/device/<device_name>')
def get_device_data(device_name):
    device_data, weather_data = collect_data()
    df = preprocess_data(device_data, weather_data)
    model = train_model(df)
    control_signals = generate_control_signals(model, device_data, weather_data)

    device_data = {
        'device_name': device_name,
        'device_details': DEVICE_DETAILS[device_name],
        'control_signal': control_signals[device_name]
    }

    return jsonify(device_data)

if __name__ == "__main__":
    app.run(debug=True)
```
