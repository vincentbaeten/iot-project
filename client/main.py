import random
import time
import ssl
import os
import json
import time
from datetime import datetime

import psutil
from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client

# Load the environment variables from the .env file
load_dotenv()

# Global variables regarding MQTT
broker = os.environ.get("BROKER_HOST")
port = int(os.environ.get("BROKER_PORT"))
base_topic = f'{os.environ.get("BASE_TOPIC")}/{os.environ.get("ASSET_ID")}'
username = os.environ.get("MQTT_USERNAME")
password = os.environ.get("MQTT_PASSWORD")
client_id = f'pynq-mqtt-{random.randint(0, 1000)}'


def get_stats() -> str:
    loadavg = psutil.getloadavg()
    virtual_mem = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")
    boot_time = psutil.boot_time()

    stats = {
        "load": {
            "1min": f'{loadavg[0]:.2f}',
            "5min": f'{loadavg[1]:.2f}',
            "15min": f'{loadavg[2]:.2f}',
        },
        "memory": {
            "percentage": virtual_mem.percent
        },
        "disk": {
            "percentage": disk_usage.percent
        },
        "uptime": int(time.time() - boot_time),
        "timestamp": datetime.now().isoformat()
    }

    return json.dumps(stats)


def connect_mqtt() -> mqtt_client.Client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code {}\n".format(rc))
    
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    # Enable TLS
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, msg):
    result = client.publish(topic, msg)

    status = result[0]

    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def publish_temperature(client: mqtt_client.Client):
    topic = f'{base_topic}/temperature'
    initial_value = 10.2
    previous = 10.2
    volatility = 0.15

    value = previous + initial_value * random.gauss(0, 1) * volatility
    previous = value

    publish(client, topic, value)


def publish_stats(client: mqtt_client.Client):
    topic = f'{base_topic}/stats'

    publish(client, topic, get_stats())


def main():
    client = connect_mqtt()
    client.loop_start()

    while True:
        publish_temperature(client)
        publish_stats(client)

        time.sleep(1)

if __name__ == '__main__':
    main()
