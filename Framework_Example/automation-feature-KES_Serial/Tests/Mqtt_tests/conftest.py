import pytest
import Config.Brewer_Config as BREWER
from Lib.MqttWrapper import MqttWrapper
import netifaces as ni

@pytest.fixture(scope='module')
def mqtt_manager():
    mqtt = MqttWrapper(get_ip())
    mqtt.connect_to_brewer()
    yield mqtt
    mqtt.disconnect()


def get_ip():
    ni.ifaddresses('eth0')
    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    return ip
