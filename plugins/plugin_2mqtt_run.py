# Command: "run" 
# author: Andrey Zobov (inspired by janvarev)

import random
from vacore import VACore
import paho.mqtt.client as mqtt
import config
import time
import sys

COMMAND_RUN = f'room/{config.ROOM_NAME}/command/run'

# ===
def mqtt_connect(subscribe) -> object:
    try:
        # creating new instance
        client = mqtt.Client(f'{config.ROOM_NAME} {time.ctime()}')
        client.username_pw_set(username=config.MQTT_USER, password=config.MQTT_PASSWORD)
        ## attach function to callback
        #client.on_message = on_message
        # connecting to broker
        client.connect(host=config.MQTT_BROKER)
        # start the loop 
        client.loop_start() 
        ##Subscribing to topic
        # client.subscribe(subscribe)
        # Done        
        return client
    except Exception as e:
        print(f'Exception "{e.__class__.__name__}" in {__file__}:{sys._getframe().f_lineno}: {e}')
        return None

    return None
# ===

# функция на старте
def start(core:VACore):
    manifest = { # возвращаем настройки плагина - словарь
        "name": "Run", # имя
        "version": "1.0", # версия
        "require_online": False, # требует ли онлайн?

        "commands": { # набор скиллов. Фразы скилла разделены | . Если найдены - вызывается функция
            "работай|работать|работа": command2mqtt
        }
    }
    return manifest

def command2mqtt(core:VACore, phrase: str): # в phrase находится остаток фразы после названия скилла,
                                              # если юзер сказал больше
                                              # в этом плагине не используется
    print("Connection to MQTT broker...")
    mqtt_client = mqtt_connect([])
    time.sleep(1)
    mqtt_client.publish(COMMAND_RUN, "")
    time.sleep(1)
    print(f'Publish "{COMMAND_RUN}" successfully.')
