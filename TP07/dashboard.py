import streamlit as st
from kafka import KafkaConsumer
import json
st.set_page_config(page_title="IoT Machine Dashboard", layout="centered")
st.title("Live Machine Monitoring")
placeholder = st.empty()
consumer = KafkaConsumer(
    'myFirstTopic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
for message in consumer:
    data = message.value
    sensor_id = data["sensor_id"]
    temperature = data["temperature"]
    engine_status = data["engine_status"]
    location = data["location"]
   
    with placeholder.container():
        st.subheader(f"Machine ID: {sensor_id}")
        st.metric(label="Temperature", value=f"{temperature} °C")
        st.metric(label="Engine Status", value=engine_status)
        st.map([{"lat": location["lat"], "lon": location["lon"]}])
        if temperature > 30:
            st.warning("Warning: Temperature is high!")
        if engine_status == "OFF":
            st.info("The engine is currently off.ً")
