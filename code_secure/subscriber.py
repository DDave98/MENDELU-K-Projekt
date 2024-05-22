import paho.mqtt.client as mqtt


broaker_addr = "broker.emqx.io"
broaker_port = 1883
broaker_keepalive = 60

# Callback funkce pro připojení
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test_sensor_data")

# Callback funkce pro příjem zpráv
def on_message(client, userdata, msg):
    print(f"topic: {msg.topic} message: {msg.payload.decode()}")

# Nastavení klienta
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Připojení k brokeru (localhost)
client.connect(broaker_addr, broaker_port, broaker_port)

# Spuštění smyčky pro zpracování zpráv
client.loop_forever()
