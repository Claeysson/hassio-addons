import json
import sys
import time
import datetime
import requests
import os

def run():
    date = datetime.datetime.now()
    print("Start at:", date)
    url = 'http://hassio/homeassistant/api/states/' + config["entity"]
    headers = {'content-type': 'application/json', 'Authorization': token}
    r = requests.get(url, headers=headers)
    json_resp = json.loads(r.text)
    
    try:
        value = json_resp["state"]
    except:
        print("Could not get temperature")
        return

    print("Temperature:", value)

    print("Reporting...")
    url = 'http://www.temperatur.nu/rapportera.php?hash=' + config["hash"] + '&t=' + value
    r = requests.get(url)

    print(r.text)



print("Starting Addon")

with open('/data/options.json', 'r') as f:
    config = json.load(f)

if config["interval"] < 30:
    print("Interval is to small.")
    print("Exit..")
    sys.exit(0)

if config["entity"] == "":
    print("No entity")
    print("Exit..")
    sys.exit(0)

if config["hash"] == "":
    print("No hash")
    sys.exit(0)

token = os.environ['HASSIO_TOKEN']


while True:
    run()
    print("Sleeping",config["interval"],"seconds")
    time.sleep(config["interval"])
    print('\n')
