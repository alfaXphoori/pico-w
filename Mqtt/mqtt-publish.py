from paho.mqtt import client as mqtt_client
import random
import time
import json
DeviceID = 101
broker = '127.0.0.1'
port = 1883
topic = "pico_sensor"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'
def connect_mqtt():
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    #client = mqtt_client.Client(client_id)
    client.username_pw_set('alfa', 'user1234')
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def temperatureVal():
    random_float = random.uniform(15, 50)
    return random_float

def humidityVal():
    random_float = random.randint(40, 90)
    return random_float

def publish(client):
    while True:
        time.sleep(1)
        temp = round(temperatureVal(),4)
        humi = int(humidityVal())

        data = [DeviceID, humi, temp,]
        msg = json.dumps(data)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"{topic}:{msg}")
        else:
            print(f"Failed to send message to topic {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()