## Exam (20 Point)

### MongoAtlas (5 Point)

1. Create Database name examdb
2. Create Collection name examauth
- Add User
  - User : exam
  - PassWD : exam

3. Create Collection name examdata
- Add Data
  - DeviceID : 1000+Student number
  - Temperature: Student number
  - Humidity: Student number

#### Streamlit Docker (5 Point)

1. Create docker Streamlit docker Port:10000+Student number
2. Create LoginPage (User from examauth)
3. Create HomePage (Data from examdata)

#### Mqtt Docker (5 Point)

1. Create Mqtt Server on Docker Port:11000+Student number
2. Create Mqtt Publish data every 5 second
*DeviceID:1000+Student number
*Temperature:Random(15-50)
*Humidity:Random(30-70)
3. Create Mqtt Subscriber Update data to MongoAtlas

#### Run Full Services (5 Point)
