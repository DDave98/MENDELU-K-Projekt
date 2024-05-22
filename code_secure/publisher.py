import paho.mqtt.client as mqtt
import sys
import time

broaker_addr = "broker.emqx.io"
broaker_port = 1883
broaker_keepalive = 60
mqttclient_id = "e87b3f516b35fd30a05512012e125e7d"

# Vytvoření klienta
client = mqtt.Client()                  
client.connect(broaker_addr, broaker_port, broaker_port)
print(f"Client created")

# Publikování zprávy na téma
client.publish("test_sensor_data", "Hello, MQTT!")
print(f"message published")

client.loop_start() # Spuštění smyčky pro zpracování zpráv
time.sleep(2)       # Čekání, aby se zpráva mohla odeslat
client.loop_stop()  # Zastavení smyčky

