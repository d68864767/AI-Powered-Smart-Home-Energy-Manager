```python
# main.py

from flask import Flask
from dashboard import app as dashboard_app
from threading import Thread
from data_collection import collect_data
from data_analysis import preprocess_data, train_model, save_model
from integration import generate_control_signals
from config import PREDICTION_INTERVAL
import time

# Function to run the data collection, analysis, and control signal generation in a loop
def run_ai_manager():
    while True:
        # Collect data
        device_data, weather_data = collect_data()

        # Preprocess data
        df = preprocess_data(device_data, weather_data)

        # Train the model
        model = train_model(df)

        # Save the model
        save_model(model, 'model.pkl')

        # Generate control signals
        control_signals = generate_control_signals(model, device_data, weather_data)

        # Sleep for the prediction interval before the next iteration
        time.sleep(PREDICTION_INTERVAL * 60)

# Function to run the dashboard
def run_dashboard():
    dashboard_app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Start the AI manager in a separate thread
    ai_manager_thread = Thread(target=run_ai_manager)
    ai_manager_thread.start()

    # Start the dashboard
    run_dashboard()
```
