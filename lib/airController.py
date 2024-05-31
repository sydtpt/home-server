import csv
import pandas as pd
from datetime import datetime, timedelta

class airController:
    
    def getAirDataframe(self):
        # Read the air.csv file and return a pandas dataframe #
        air_history = pd.read_csv('./data/air.csv')
        air_history['timestamp'] = pd.to_datetime(air_history['timestamp'])
        return air_history
    
    def max_temperature(self,last_hours=None):
        # Get the maximum temperature from the last n hours #
        if last_hours is None:
            air_history = self.getAirDataframe()
        else:
            air_history = self.filteredByHours(last_hours)
        max_temperature = air_history['temperature'].max()
        return int(max_temperature)

    def temperature(self):
        # Get the maximum temperature from the last n hours #
        air_history = self.getAirDataframe()
        print(air_history)
        temper = 17
        return temper
    def humidity(self):
        # Get the maximum temperature from the last n hours #
        air_history = self.getAirDataframe()
        print(air_history)
        humidity = 63
        return humidity

    def avg_temperature( self,last_hours=None):
        if last_hours is None:
            air_history = self.getAirDataframe()
        else:
            air_history = self.filteredByHours(last_hours)
        avg_temperature = round(air_history['temperature'].mean(), 1)
        return float(avg_temperature)

    def max_humidity(self,last_hours=None):
        if last_hours is None:
            air_history = self.getAirDataframe()
        else:
            air_history = self.filteredByHours(last_hours)
        max_humidity = air_history['humidity'].max()
        return int(max_humidity)

    def avg_humidity(self,last_hours=None):
        if last_hours is None:
            air_history = self.getAirDataframe()
        else:
            air_history = self.filteredByHours(last_hours)
        avg_humidity = round(air_history['humidity'].mean(), 1)
        return float(avg_humidity)
    
    def log(self, temperature: float, humidity: float):
        with open("./data/air.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([temperature, humidity, datetime.now()])
            f.close()
        return True
    
    def filteredByHours(self, last_hours: int):
        # Return a dataframe with the air history by the last N hours #
        air_history = self.getAirDataframe()
        now = datetime.now()
        filteredAirHistory = now - timedelta(hours=last_hours)
        filtered_df = air_history[air_history['timestamp'] >= filteredAirHistory]
        return filtered_df
    

