## Exam (20 Point)
### MongoAtlas                  (6 Point)
1. Create Database name examdb
![spc1-1](https://github.com/user-attachments/assets/4de5e179-1cb0-4e79-9155-93b2042b3915)
2. Create Collection name examauth
- Add User
  - User : exam
  - PassWD : exam
![spc1-2](https://github.com/user-attachments/assets/04ddc3e0-1bca-43b3-b2cb-415079416fe6)
3. Create Collection name examdata
- Add Data
  - DeviceID : 1000+Student number
  - Temperature: Student number
  - Humidity: Student number
![spc1-3](https://github.com/user-attachments/assets/be4d2a4e-9616-4262-8e81-118e03426f5e)
#### Streamlit Docker           (6 Point)
1. Create docker Streamlit docker Port:10000+Student number
2. Create LoginPage (User from examauth)
3. Create HomePage (Data from examdata)

#### Mqtt Docker                (6 Point)
1. Create Mqtt Server on Docker Port:11000+Student number
2. Create Mqtt Publish data every 5 second
*DeviceID:1000+Student number
*Temperature:Random(15-50)
*Humidity:Random(30-70)
3. Create Mqtt Subscriber Update data to MongoAtlas

#### Run Full Services          (2 Point)
