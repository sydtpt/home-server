from flask import request
import pandas as pd
import http.client

import requests

class deviceController:
    def getDevices(self):
        devices_df = pd.read_csv('./data/devices.csv')
        return devices_df
    
    
    def getDomain(self,name: str):
        devices_df = self.getDevices()
        filtered_df = devices_df[devices_df['name'] == name]
        domain = filtered_df.loc[0].domain
        return domain
    
    def getStatus(self,name: str):
        ip = self.getDomain(name)
        conn = http.client.HTTPConnection(ip)
        conn.request("GET", "/relay/0")
        response = conn.getresponse()
        conn.close()
        return response
    
    def turnOn(self,name: str):
        ip = self.getDomain(name)
        conn = http.client.HTTPConnection(ip)
        conn.request("GET", "/relay/0?turn=on")
        response = conn.getresponse()
        conn.close()
        return response
            
    def turnOff(self,name: str):
        ip = self.getDomain(name)
        conn = http.client.HTTPConnection(ip)
        conn.request("GET", "/relay/0?turn=off")
        response = conn.getresponse()
        conn.close()
        return response
    
    def get_device_status(self, ip: str):
        response = requests.get(f'http://{ip}/relay/0')
        try:
            body = response.json()
            print("##############")
            print("##############")
            print("##############")
            print(body)
            print(body['ison'])
            print("##############")
            print("##############")
            print("##############")
            return body['ison'] == True
        except:
            return False