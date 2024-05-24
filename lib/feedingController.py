import csv
import pandas as pd
from datetime import datetime, timedelta

class feedingController:
    def lastSoilFeeding(name):
        air_history = pd.read_csv('./data/soil-fert.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        filtered_df = air_history[air_history['name'] == name]
        lastFert = filtered_df['timestamp'].max()
        now = datetime.now()
        daysDiff = datetime.now() - lastFert
        return str(daysDiff.days) + "d"
    
    def lastLeafFeeding(name):
        air_history = pd.read_csv('./data/leaf-fert.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        filtered_df = air_history[air_history['name'] == name]
        lastFert = filtered_df['timestamp'].max()
        now = datetime.now()
        daysDiff = datetime.now() - lastFert
        return str(daysDiff.days) + "d"
    
    def lastSoilWatter(name):
        air_history = pd.read_csv('./data/watering.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        filtered_df = air_history[air_history['name'] == name]
        lastFert = filtered_df['timestamp'].max()
        now = datetime.now()
        daysDiff = datetime.now() - lastFert
        return str(daysDiff.days) + "d"    
