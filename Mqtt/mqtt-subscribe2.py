import random
from paho.mqtt import client as mqtt_client
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://alfa:user1234@cecluster.x6mxg.mongodb.net/?retryWrites=true&w=majority&appName=CeCluster"
client = MongoClient(uri)
database = client["ceiot"]
collection_auth = database["auth"]
collection_devices = database["devices"]

broker = '127.0.0.1'
port = 1883
topic = "pico_sensor"
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    #client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #print("deviceID: ",msg.payload.decode()[1:4])
        deviceID = int(msg.payload.decode()[1:4]) 
        #temperature = float(msg.payload.decode()[9:15])
        #print(msg.payload.decode())
        #print(len(msg.payload.decode()))
        if(len(msg.payload.decode())==17):
            temperature = float(msg.payload.decode()[9:15])
            print("Temperature: ",temperature)
        else:
            temperature = float(msg.payload.decode()[9:14])
            print("Temperature: ",temperature)

        senser_val = {
        "device":deviceID,
        "type":"sensor",
        "temperature": temperature
        }
        #collection_devices.insert_one(senser_val)
        #print(senser_val)
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()