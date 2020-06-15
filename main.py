import paho.mqtt.client as paho
import os
import json
import logging

# .ENV FILE FOR TESTING
#if os.path.exists('.env'):
#    from dotenv import load_dotenv
#    load_dotenv()

# GLOBALS
MQTT_BROKER = os.environ.get('MQTT_BROKER','')
MQTT_PORT = int(os.environ.get('MQTT_PATH', 1883))
MQTT_PUB_TOPIC = os.environ.get('MQTT_PUB_TOPIC','')
MQTT_SUB_TOPIC = os.environ.get('MQTT_SUB_TOPIC','')
INPUT_PATH = os.environ.get('INPUT_PATH','input')

BASE_DIR = os.getcwd()
INPUT_PATH = os.path.join(BASE_DIR, INPUT_PATH)

def delete_file(file_name):
    file_name = os.path.join(INPUT_PATH, file_name)
    logging.debug("file_name : {}".format(file_name)) 
    if os.path.exists(file_name):
        logging.debug("file exists : True") 
        try:
            logging.debug("Try file delete") 
            os.remove(file_name)
        except:
            logging.info("couldnt delete file {}".format(file_name))

# SUB MQTT
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_SUB_TOPIC)

def on_message(client, userdata, msg):
    logging.info("Received : {} convert to json".format(str(msg.payload))) 
    message = msg.payload.decode('utf-8')
    logging.debug("message : {}".format(str(message))) 
    message = json.loads(message)
    file_name = message['pathToImage']
    logging.debug("json_image : {}".format(str(file_name)))
    delete_file(file_name)

def main():
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info("STARTING MQTT RM Bot")
    client = paho.Client("mqtt-rmbot")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

# Main Exectution
main()
