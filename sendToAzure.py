import paho.mqtt.client as mqtt
import json
from datetime import datetime
import requests
import os

URL = "pavliskomiot2021.westeurope.cloudapp.azure.com/api/telemetry/measurement" 
def on_connect(client, userdata, flags, rc):
    print("connected")

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subbed")

def on_message(client, userdata, msg):
    print("Topic receieved")
    handle_mqtt_data(msg.topic, msg.payload.decode('utf-8'))

def handle_mqtt_data(topic, payload):
    print("Handling data")
    json_data = dict()

    try:
        if "temperature" in topic and "mpavlisko" in topic:
            json_data["SensorName"] = "temperature"
            json_data["SensorValue"] = str(float(payload))
            json_data["DeviceId"] = 1
        elif "heartrate" in topic and "mpavlisko" in topic:
            json_data["SensorName"] = "heartrate"
            json_data["SensorValue"] = str(float(payload))
            json_data["DeviceId"] = 1
        elif "battery" in topic and "mpavlisko" in topic:
            json_data["SensorName"] = "battery"
            json_data["SensorValue"] = str(float(payload))
            json_data["DeviceId"] = 1
        else:
            print("Received an unknown message")

    except Exception as e:
        print("Encountered an error", e)

    json_data["CreatedOn"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(json_data)
    json_string = json.dumps(json_data)
    print(json_data)
    post_data(json_data)

def post_data(json_string):
    response = requests.post(URL, json=json_string)
    if response.status_code == 200:
        print("Poslano")
    else:
        print("Nesto ne radi")

if __name__ == "__main__":
        print("eee")
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.connect("127.0.0.1", 1883)
        client.subscribe("algebra/iot/mpavlisko/#")
        client.loop_forever()