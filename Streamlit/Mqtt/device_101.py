import random

DeviceID = 101
def temperatureVal():
    random_float = random.uniform(20, 50)
    return random_float

print(DeviceID, temperatureVal())