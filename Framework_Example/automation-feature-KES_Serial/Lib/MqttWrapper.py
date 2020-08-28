"""
This file is a wrapper for all of MQTT functionality. Handling connection, subscribing, publishing, and *callbacks*

"""
import paho.mqtt.client as mqtt
import Lib.GLOBALS.MQTT_TOPICS as MQTT_TOPICS
import time


class MqttWrapper:

    def __init__(self, IP):
        """
        Class init
        """
        self.IP = IP
        self.port = 1883
        self.brewer_connection = None

    @staticmethod
    def on_publish(client, userdata, result):  # create function for callback
        print("result of publish is: {}".format(result))

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("result code " + str(rc))

    @staticmethod
    def on_message(client, obj, msg):
        print("message is: " + msg.topic + " " + str(msg.payload))

    @staticmethod
    def on_subscribe(client, obj, mid, granted_qos):
        print("subscribed {}".format(str(mid)))

    @staticmethod
    def everything_callback(client, userdata, message):
        print("######################")
        print("Message payload is: {}".format(message.payload))
        print("message topic is: {}".format(message.topic))
        print("######################")

    def connect_to_brewer(self):
        """
        Establishes connection to brewer MQTT broker
        """
        self.brewer_connection = mqtt.Client('brewerClient')
        self.brewer_connection.on_connect = self.on_connect
        self.brewer_connection.on_publish = self.on_publish
        self.brewer_connection.on_subscribe = self.on_subscribe
        self.brewer_connection.on_message = self.on_message
        for i in MQTT_TOPICS.POWDER_DISPENSE_PROXY_SUBSCRIBE:
            self.brewer_connection.message_callback_add(i, self.everything_callback)
        self.brewer_connection.loop_start()
        self.brewer_connection.connect(self.IP, self.port)
        time.sleep(3)
        for i in MQTT_TOPICS.POWDER_DISPENSE_PROXY_SUBSCRIBE:
            self.brewer_connection.subscribe(i)

    def publish(self, topic, payload):
        """
        Publishes payload to topic
        """
        self.brewer_connection.publish(topic, payload)
        time.sleep(2)

    def disconnect(self):
        self.brewer_connection.disconnect()
