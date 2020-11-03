import json
# from rancidcmd import RancidCmd
import os
import sys
import time
from pprint import pprint
import requests
from requests.packages import urllib3
from pprint import pprint
import mysql.connector
from os import path
import logging
import mysql.connector

class inventory():
    def __init__(self):
        try:
            path_file = path.dirname(path.abspath(__file__))
            file_name = path.join(path_file,"config.json")
            with open (file_name,"r") as config_file:
                self.config = json.load(config_file)
                self.urltoken = self.config["inventory"]["url_token"]
                self.urldata = self.config["inventory"]["url_data"]
                self.payload = self.config["inventory"]["payload"]
                self.header_token = self.config["inventory"]["header_token"]
        except Exception as e:
            raise e
    def getdata_inventory(self):
        try:
            token_text = requests.get(self.urltoken, headers=self.header_token, data=self.payload, verify=False)
            reponse = eval(token_text.text)
            if "token" in reponse:
                ops_token = reponse["token"]
                #print ops_token
            data_inventory = requests.get(
                self.urldata,
                headers={
                    "Accept": "application/json",
                    "Content-type":"application/x-www-form-urlencoded",
                    "Authorization":"Bearer " + ops_token
                },
                verify = false
            )
            device_inventory = json.loads(data_inventory.text)
            return device_inventory
        except Exception as e:
            raise e

