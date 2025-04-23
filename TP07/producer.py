from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
def get_random_location():
    lat = round(random.uniform(36.70, 36.73), 6)
    lon = round(random.uniform(7.28, 7.30), 6)
    return lat, lon

while True:
    temperature = round(random.uniform(20.0, 35.0), 2)
    engine_status = random.choice(["ON", "OFF"])
    lat, lon = get_random_location()

    data = {
        'sensor_id': 'machine-01',
        'temperature': temperature,
        'engine_status': engine_status,
        'location': {'lat': lat, 'lon': lon}
    }

    print(f"Sending: {data}")
    producer.send('myFirstTopic', value=data)
    time.sleep(2)
