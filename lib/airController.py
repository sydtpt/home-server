import csv
import pandas as pd
from datetime import datetime, timedelta

class airController:
    def max_temperature(last_hours: int):
        air_history = pd.read_csv('./data/air.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        now = datetime.now()
        filteredAirHistory = now - timedelta(hours=last_hours)
        filtered_df = air_history[air_history['timestamp'] >= filteredAirHistory]
        max_temperature = filtered_df['temperature'].max()
        return int(max_temperature)

    def avg_temperature( last_hours: int):
        air_history = pd.read_csv('./data/air.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        now = datetime.now()
        filteredAirHistory = now - timedelta(hours=last_hours)
        filtered_df = air_history[air_history['timestamp'] >= filteredAirHistory]
        avg_temperature = round(filtered_df['temperature'].mean(), 1)
        return float(avg_temperature)

    def max_humidity( last_hours: int):
        air_history = pd.read_csv('./data/air.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        now = datetime.now()
        filteredAirHistory = now - timedelta(hours=last_hours)
        filtered_df = air_history[air_history['timestamp'] >= filteredAirHistory]
        max_humidity = filtered_df['humidity'].max()
        return int(max_humidity)

    def avg_humidity( last_hours: int):
        air_history = pd.read_csv('./data/air.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        now = datetime.now()
        filteredAirHistory = now - timedelta(hours=last_hours)
        filtered_df = air_history[air_history['timestamp'] >= filteredAirHistory]
        avg_humidity = round(filtered_df['humidity'].mean(), 1)
        return float(avg_humidity)
    
    def log( temperature: float, humidity: float):
        with open("./data/air.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([temperature, humidity, datetime.now()])
            f.close()
        return True
    
    
