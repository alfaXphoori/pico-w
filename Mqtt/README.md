
## MQTT

#### Create Directory config
- add mosquitto.conf
```bash
allow_anonymous false
listener 1883
listener 9001
protocol websockets
persistence true
password_file /mosquitto/config/pwfile
persistence_file mosquitto.db
persistence_location /mosquitto/data/
```
- add pwfile

#### Run Docker compose
```bash
docker compose up -d
```

#### Create User MQTT
```bash
docker exec -it mosquitto sh
```
- Create new user name alfa
```bash
mosquitto_passwd -c /mosquitto/config/pwfile alfa
```
- exit

#### Run MQTT Publish
```bash
python mqtt-publish.py
```

#### Run MQTT Subscribe.py
```bash
python mqtt-subscribe.py
```


