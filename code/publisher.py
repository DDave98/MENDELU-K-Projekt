import paho.mqtt.client as mqtt
import time

# Vytvoření klienta
id="e87b3f516b35fd30a05512012e125e7d"
client = mqtt.Client(client_id=id)                  
client.connect("127.0.0.1", 1883, 60)   # Připojení k brokeru (localhost)

# Publikování zprávy na téma
client.publish("test/topic", "Hello, MQTT!")

client.loop_start() # Spuštění smyčky pro zpracování zpráv
time.sleep(2)       # Čekání, aby se zpráva mohla odeslat
client.loop_stop()  # Zastavení smyčky
