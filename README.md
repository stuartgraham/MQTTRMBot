# MQTT RM Bot
Takes MQTT messages with jpg path and deletes file

### Environment variables
Pass the following environment vairables to execution environment
| Settings | Description | Inputs |
| :----: | --- | --- |
| `MQTT_BROKER` | MQTT Broker address | `mqtt.test.local` |
| `MQTT_PORT` | MQTT Broker port | `1883` |
| `MQTT_SUB_TOPIC` | MQTT Topic to subscribe to | `test/messages` |
| `INPUT_PATH` | Sub directory with input files | `input` |


### Requirements
```sh
pip install -p requirements.txt
```

### Execution 
```sh
python3 .\main.py
```

### Docker Compose
```sh 
  mqttrmbot:
      image: stuartgraham/mqttrmbot
      container_name: mqttrmbot
      environment:
          - INPUT_PATH=input
          - MQTT_BROKER=mqtt.test.local
          - MQTT_PORT=1883
          - MQTT_SUB_TOPIC=cctv/delete
      volumes:
          - input-storage:/app/input:rw
      restart: always

```

