from Lib.MqttWrapper import MqttWrapper
import Lib.GLOBALS.MQTT_TOPICS as TOPICS


def test_appliance_state_machine():
    """
    testing script given by AFH team. Needs powder board to be ran
    """
    mqtt_manager = MqttWrapper()
    mqtt_manager.connect_to_brewer()
    mqtt_manager.publish(TOPICS.ASP_WORKFLOWID, "1")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BREWTYPE, "1")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BEVERAGEPOWDERRATIO, "50")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_TOTALVOLUMEML, "240")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_FLOWRATEMLM, "295")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_BREWTEMPCELSIUS, "90")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_HWTTEMPCELSIUS, "71")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_AIRPURGETIMEMS, "5000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_ENABLE, "1")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AIRPURGETIMEMS, "6000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_TSTARTMS, "1000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_TDURATIONMS, "10000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_MIXRATIO, "40")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_MIXPWM, "20")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_FROTHPWM, "80")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AUGER_TSTARTMS, "2000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AUGER_TDURATIONMS, "8000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AUGER_PWM, "10")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_ENABLE, "0")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AIRPURGETIME, "3000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_TSTARTMS, "21")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_TDURATIONMS, "22")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_MIXRATIO, "23")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_MIXPM, "24")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_FROTHPWM, "25")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AUGER_TSTARTMS, "26")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AUGER_TDURATIONMS, "27")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AUGER_PWM, "28")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_FAN_ONOFF, "29")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_FAN_IDLESPEEDPWM, "30")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_FAN_DISPENSESPEEDPW, "31")
    mqtt_manager.publish(TOPICS.ASP_BREWSTART, "32")


def test_powder_logic():
    """
    Powder logic test to valid Orchestrator
    """
    mqtt_manager = MqttWrapper()
    mqtt_manager.connect_to_brewer()
    mqtt_manager.publish(TOPICS.ASP_WORKFLOWID, "1")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BREWTYPE, "1")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BEVERAGEPOWDERRATIO, "50")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_TOTALVOLUMEML, "240")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_FLOWRATEMLM, "295")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_BREWTEMPCELSIUS, "90")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_HWTTEMPCELSIUS, "71")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_BE_AIRPURGETIMEMS, "5000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_ENABLE, "1")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AIRPURGETIMEMS, "6000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_TSTARTMS, "1000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_TDURATIONMS, "10000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_MIXRATIO, "40")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_MIXPWM, "20")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_WHIPPER_FROTHPWM, "80")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AUGER_TSTARTMS, "2000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AUGER_TDURATIONMS, "8000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_1_AUGER_PWM, "10")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_ENABLE, "0")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AIRPURGETIME, "3000")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_TSTARTMS, "21")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_TDURATIONMS, "22")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_MIXRATIO, "23")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_MIXPM, "24")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_WHIPPER_FROTHPWM, "25")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AUGER_TSTARTMS, "26")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AUGER_TDURATIONMS, "27")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_POWDER_2_AUGER_PWM, "28")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_FAN_ONOFF, "29")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_FAN_IDLESPEEDPWM, "30")
    mqtt_manager.publish(TOPICS.ASP_WORKFLOW_FAN_DISPENSESPEEDPW, "31")
    mqtt_manager.publish(TOPICS.ASP_BREWSTART, "32")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "2")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "4")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "5")
    mqtt_manager.publish(TOPICS.PWD_DISP_PRXY_OUT_0_ENCODER_REV, "TRUE")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "6")
    mqtt_manager.publish(TOPICS.PWD_DISP_PRXY_OUT_2_ENCODER_REV, "TRUE")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "7")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "8")
