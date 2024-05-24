import csv
import http.client
import pandas as pd
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import asyncio
    
class scheduleController:
    def delete_line(self, index, filename = "./data/schedule.csv"):
        with open(filename, 'r') as f:
            lines = f.readlines()
        if index < len(lines):
            del lines[index]

        with open(filename, 'w') as f:
            f.writelines(lines)
            
    def getSchedule(self):
        schedule = pd.read_csv('./data/schedule.csv')
        return schedule
    
    def add(self, value: bool, device: str, hour: str):
        with open("./data/schedule.csv", 'a') as f:
            writer = csv.writer(f)
            writer.writerow([value, device, hour])
            f.close()
        return True
    
    def delete(self, index: int):
        self.delete_line(index)
    
    def getElegibleTasks(self):
        lastMinutes = datetime.now() - timedelta(minutes=10)
        lastMinutes_str = lastMinutes.strftime('%H:%M')
        schedule = self.getSchedule()
        filtered_schedule = schedule[(schedule['hour'] >= lastMinutes_str) & (schedule['hour'] <= datetime.now().strftime('%H:%M'))]
        return filtered_schedule
    
    def scheduled_task(self):
        print("Looking for tasks to execute.")
        tasks = self.getElegibleTasks()
        for index, row in tasks.iterrows():
            print(f"Device: {row['device']} - Value: {row['action']} - Hour: {row['hour']}")
            if row['device'] == 'sansi' and row['action'] == 1:
                print("Turning on")
                conn = http.client.HTTPConnection("192.168.1.8")
                conn.request("GET", "/relay/0?turn=on")
                response = conn.getresponse()
                data = response.read()
                print(data)
                conn.close()
            if row['device'] == 'sansi' and row['action'] == 0:
                print("Turning off")
                conn = http.client.HTTPConnection("192.168.1.8")
                conn.request("GET", "/relay/0?turn=off")
                response = conn.getresponse()
                data = response.read()
                print(data)
                conn.close()

    def start_scheduler(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.scheduled_task, IntervalTrigger(minutes=5))
        asyncio.run(scheduler.start())
        print("Setting up scheduler.3")
        return
