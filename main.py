import webpy.web as web
import requests
import sqlite3
import os
import sys
import time
import xml.etree.ElementTree as ET

PATH = os.path.abspath(os.path.dirname(sys.argv[0])) # The path of this file
timer=os.times()
web.config.debug = False # Set true to open debug output
urls=(
    '/','handler'
)

database = sqlite3.connect(PATH+r"\data.db") # Initializing database
#database_dir = PATH+r"\..\Static\appid.db"
#database = web.database(dbn="sqlite",db=database_dir)
# Create table to store tokens
try:
    database.execute('''CREATE TABLE user_rawdata(id text,  yaw real, pitch real, roll real, ax real, ay real, az real, date test,time text)''') # User's raw data
    # database.execute('''CREATE TABLE user_data(id text, state text, time text)''') # User's state
except:
    del database

class handler():
    db = None
    def __init__(self):
        handler.db = web.database(dbn="sqlite",db=PATH+r"\data.db")
    def GET(self): # ip:8080?id= &date=
        # id, date = web.input()["id"],web.input()["date"] # date should be the same as the date in xml pkg
        return "Ha"# 24 hrs state
    def POST(self):
        xml_data = web.data().decode()
        # Parse xml
        # print(xml_data)
        xml_root = ET.fromstring(xml_data)
        data = [(i.tag,i.text) for  i in xml_root]
        user_data=dict(data)
        handler.db.query("INSERT INTO user_rawdata VALUES($id,$yaw,$pitch,$roll,$ax,$ay,$az,$date,$time)",vars=user_data)
        print(time.strftime("%Y-%m-%d %H:%M:%S"),xml_root.find("id").text,"POST data",user_data)

        return "Success"
        # Access to ML and get and store in sql

if __name__ == "__main__":
    app=web.application(urls,globals())
    app.run()