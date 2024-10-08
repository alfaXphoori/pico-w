import random

DeviceID = 101
def temperatureVal():
    random_float = random.uniform(15, 50)
    return random_float

print(DeviceID, temperatureVal())