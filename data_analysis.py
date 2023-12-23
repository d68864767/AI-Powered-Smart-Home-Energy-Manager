```python
# data_analysis.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

# Function to preprocess the collected data
def preprocess_data(device_data, weather_data):
    # Convert the data to pandas DataFrame
    device_df = pd.DataFrame(device_data)
    weather_df = pd.DataFrame(weather_data)

    # Merge the two dataframes
    merged_df = pd.concat([device_df, weather_df], axis=1)

    # Drop any rows with missing values
    merged_df.dropna(inplace=True)

    return merged_df

# Function to train the model
def train_model(df):
    # Define the target variable and the feature variables
    y = df['energy_usage']
    X = df.drop('energy_usage', axis=1)

    # Split the data into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict the energy usage
    y_pred = model.predict(X_test)

    # Evaluate the model
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    return model

# Function to save the trained model
def save_model(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

# Main function to preprocess the data and train the model
def analyze_data(device_data, weather_data):
    df = preprocess_data(device_data, weather_data)
    model = train_model(df)
    save_model(model, 'model.pkl')

if __name__ == "__main__":
    device_data, weather_data = collect_data()
    analyze_data(device_data, weather_data)
```
