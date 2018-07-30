import paho.mqtt.client as mqtt
from flask import Flask, jsonify

from prometheus_client import Gauge, start_http_server

data = {}

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe("#")

def on_message(client, userdata, msg):
    parsed = None
    name = msg.topic.replace("/", "_").replace(" ", "_").lower()
    incoming = msg.payload.decode()
    try:
        parsed = float(incoming)
        if parsed.is_integer():
            parsed = int(incoming)
    except ValueError:
        if incoming == "off" or incoming == "inactive":
            parsed = 0
        elif incoming == "on" or incoming == "active":
            parsed = 1
        else:
            print(f"{name} state {incoming} not supported")
            return
    if name not in data:
        data[name] = Gauge(name, msg.topic)
    data[name].set(parsed)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
start_http_server(9094)

client.loop_forever()

