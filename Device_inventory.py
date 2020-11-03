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
                self.header = self.config["inventory"]["header"]
        except Exception as e:
            raise e
