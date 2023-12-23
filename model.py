```python
# model.py

import pickle
from sklearn.linear_model import LinearRegression
from data_collection import collect_data
from data_analysis import preprocess_data

# Function to train the model
def train_model(df):
    # Define the target variable and the feature variables
    y = df['energy_usage']
    X = df.drop('energy_usage', axis=1)

    # Train the model
    model = LinearRegression()
    model.fit(X, y)

    return model

# Function to save the trained model
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

# Main function to collect data, preprocess it, train the model, and save the model
def main():
    device_data, weather_data = collect_data()
    df = preprocess_data(device_data, weather_data)
    model = train_model(df)
    save_model(model, 'model.pkl')

if __name__ == "__main__":
    main()
```
