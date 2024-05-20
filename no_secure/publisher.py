import paho.mqtt.client as mqtt
import time


client = mqtt.Client()                  # Vytvoření klienta
client.connect("localhost", 1883, 60)   # Připojení k brokeru (localhost)

# Publikování zprávy na téma
client.publish("test/topic", "Hello, MQTT!")

client.loop_start() # Spuštění smyčky pro zpracování zpráv
time.sleep(2)       # Čekání, aby se zpráva mohla odeslat
client.loop_stop()  # Zastavení smyčky
