from phew import server, connect_to_wifi
import machine
import json

ip = connect_to_wifi("SSID", "PASSWD")

print("connected to IP ", ip)

@server.route("/api/pico_get", methods=["GET"])
def get_data(request):
    data = "Phoori"
    return json.dumps({"pico_get" : data}), 200, {"Content-Type": "application/json"}

@server.route("/api/pico_post", methods=["POST"])
def post_data(request):
    data = (request.data["wpost"])
    print(data)
    return json.dumps({"message" : "Command sent successfully!"}), 200, {"Content-Type": "application/json"}

@server.catchall()
def catchall(request):
    return json.dumps({"message" : "URL not found!"}), 404, {"Content-Type": "application/json"}

server.run()
