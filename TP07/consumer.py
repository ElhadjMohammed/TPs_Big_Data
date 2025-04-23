from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'myFirstTopic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))

)

for message in consumer:
    data = message.value
    sensor_id = data["sensor_id"]
    temperature = data["temperature"]
    engine_status = data["engine_status"]
    location = data["location"]

    print(f"------------ New message --------------")
    print(f"ID: {sensor_id}")
    print(f"the heat: {temperature} °C")
    print(f"Engine condition: {engine_status}")
    print(f"Location: Latitude {location['lat']}, Longitude {location['lon']}")
    print("-------------------------------------------------------------------\n")
