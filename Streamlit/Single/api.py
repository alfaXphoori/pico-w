from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://alfa:user1234@cecluster.x6mxg.mongodb.net/?retryWrites=true&w=majority&appName=CeCluster"
client = MongoClient(uri)
database = client["ceiot"]
collection_auth = database["auth"]
collection_devices = database["devices"]

last_data = collection_devices.find({"type":"sensor"},sort=[('_id',-1)]).limit(10)
data = []
for val in last_data:
        val = str(val["temperature"])  # Convert ObjectId to string
        data.append(val)
print (data)

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>CE Api</p>"

# Route to login user (POST username and password)
@app.route('/login', methods=['POST'])
def login_user():
    data = request.json  # Get the JSON payload
    username = data.get('username')
    password = data.get('password')
    print(data)

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = collection_auth.find_one(
        {"username":"test",
         "password":"test"
         })
    print(user)

    if user:
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/sensor', methods=['GET'])
def device_sensor():
    data = collection_devices.find_one({"type":"sensor"},sort=[('_id', -1)])
    sensor_data = {"device":data["device"],
                   "temperature":data["temperature"],
                   "humidity":data["humidity"]
                   }
    return jsonify(sensor_data)

@app.route('/control', methods=['POST'])
def device_control():
    data = request.json
    control_data = {
        "device":20001,
        "type":"control",
        "con1": data["con1"],
        "con2": data["con2"],
    }
    collection_devices.insert_one(control_data)
    return jsonify({'message':'Add Done'})

@app.route('/chart', methods=['GET'])
def device_ten_sensor():
    last_data = collection_devices.find({"type":"sensor"},sort=[('_id',-1)]).limit(10)
    data = []
    for val in last_data:
        val = str(val["temperature"])  # Convert ObjectId to string
        data.append(val)
    return data