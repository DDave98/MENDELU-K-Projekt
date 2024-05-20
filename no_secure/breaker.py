import paho.mqtt.client as mqtt

# Callback funkce pro připojení
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

# Callback funkce pro příjem zpráv
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}")

# Nastavení klienta
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
print(f"Breaker Client Created")

# Připojení k brokeru (localhost)
client.connect("localhost", 1883, 60)

# Spuštění smyčky pro zpracování zpráv
client.loop_forever()