import json
# from rancidcmd import RancidCmd
import os
import sys
import time
from pprint import pprint
import requests
from requests.packages import urllib3
from pprint import pprint
from os import path
import logging


class portnet():
    def __init__(self):
        try:
            path_file = path.dirname(path.abspath(__file__))
            file_name = path.join(path_file,"config.json")
            with open (file_name,"r") as config_file:
                self.config = json.load(config_file)
                self.urldata = self.config["portnet"]["url_data"]
                self.header = self.config["portnet"]["header"]
        except Exception as e:
            raise e
    def getdevice_portnet(self):
        try:
            data_portnet = requests.get(self.urldata, headers = self.header, verify = False)
            device_portnet = json.loads(data_portnet.text)
            return device_portnet
        except Exception as e:
            raise e

        