import json
import Lib.GLOBALS.MQTT_TOPICS as TOPICS
import pytest
import time

@pytest.mark.TM_3564
def test_powder_logic(mqtt_manager):
    """
    Powder logic test to valid Orchestrator
    """
    mqtt_manager.publish(TOPICS.AM_WORKFLOWID, "1")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_BREWTYPE, "1")
    mqtt_manager.publish(TOPICS.AM_DISPENSEORDER, "1,2,3")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_PCTVOLUME, "50")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_BE_TOTALVOLUMEML, "240")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_BE_FLOWRATEMLM, "295")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_BE_BREWTEMPCELSIUS, "90")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_BE_HWTTEMPCELSIUS, "71")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_BE_AIRPURGETIMEMS, "5000")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_ENABLE, "1")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_AIRPURGETIMEMS, "6000")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_FLOWMLM, "480")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_FLOWMGM, "100")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_PCTVOL, "25")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_VOLMG, "18")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_BREWTEMPC, "10")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_WHIP_FROTHRATIO, "50")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_1_WHIP_FROTHDENSTIY, "froth_medium")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_ENABLE, "1")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_AIRPURGETIME, "6000")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_FLOWMLM, "480")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_FLOWMGM, "100")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_PCTVOL, "25")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_VOLMG, "18")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_BREWTEMPC, "10")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_WHIP_FROTHRATIO, "50")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_POWDER_2_WHIP_FROTHDENSTIY, "froth_medium")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_FAN_ONOFF, "29")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_FAN_IDLESPEEDPWM, "30")
    mqtt_manager.publish(TOPICS.AM_WORKFLOW_FAN_DISPENSESPEEDPWM, "31")
    mqtt_manager.publish(TOPICS.AM_BREWSTART, "32")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "2")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "4")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "5")
    mqtt_manager.publish(TOPICS.PWD_DISP_PRXY_OUT_0_ENCODER_REV, "true")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "6")
    mqtt_manager.publish(TOPICS.PWD_DISP_PRXY_OUT_2_ENCODER_REV, "true")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "7")
    mqtt_manager.publish(TOPICS.BREWER_SYNC_WORKFLOW_STATE, "8")
    mqtt_manager.disconnect()

@pytest.mark.TM_3655
def test_brew_twin_messages(mqtt_manager):
    start_brew_message = json.dumps({"beverageData": {"timestamp": "2020-07-02T11:29:13", "beverageUid": 54742, "recognitionResult": {"brand": "TEST_BRAND", "variety": "TEST_VARIETY", "file": "<file>", "data": {}}, "brand": "TEST_BRAND", "variety": "TEST_VARIETY", "beverageType": "Vanilla Coffee", "beverageSizeOz": 4, "default": True, "brewId": 2, "recipeConstraints": { "powderType": {"excludeSizesOz": [], "excludeStrength": [], "excludeTemp": [], "excludeTypes": [], "powderType": ["Chocolate", "Milk", "Vanilla"]}}, "recipe": {"criticalParameters": {"beverageSize": 4, "beverageType": "Vanilla Coffee", "brandName": "Dunkin®", "customStrength": "Strong", "customTemperature": "Hotter", "isDefault": False, "isRecommended": False, "varietyName": "Dunkin Decaf®"}, "dispenseSteps": [{"dispenseType": "Needle", "dispenseStepNumber": 0, "needleParameters": {"isEnhanced": False, "waterFlowrate": 12.5, "waterSource": "Hot Water", "waterTemperature": 198, "waterVolumePC": 95}}, {"dispenseType": "Powder", "dispenseStepNumber": 1, "powderParameters": {"frothDensity": "Medium", "frothRatioPC": 10, "powderMass": 5.0, "powderType": "Vanilla", "waterFlowrate": 12.5, "waterTemperature": 198, "waterVolumePC": 5}}, {"dispenseType": "Syrup", "dispenseStepNumber": 2, "syrupParameters": {"syrupType": "French Vanilla", "syrupVolume": 10}}, {"dispenseType": "Syrup", "dispenseStepNumber": 3, "syrupParameters": {"syrupType": "Vanilla", "syrupVolume": 10}}, {"dispenseType": "Syrup", "dispenseStepNumber": 4, "syrupParameters": {"syrupType": "Hazelnut", "syrupVolume": 10}}]}}})
    end_brew_message = json.dumps({"beverageData": {"timestamp": "2020-07-02T11:29:13", "beverageUid": 33103, "recognitionResult": {"brand": "TEST_BRAND", "variety": "TEST_VARIETY", "file": "<file>", "data": {}}, "brand": "TEST_BRAND", "variety": "TEST_VARIETY", "beverageType": 4, "beverageSizeOz": 4, "default": True, "brewId": 2, "recipeConstraint": {"powderType": [], "excludeSizesOz": [4, 6], "excludeTypes": ["powderType1", "powderType2"], "excludeStrength": ["s1", "s2"], "excludeTemp": ["t1", "t2"]}, "recipe": {"criticalParameters": {"beverageSize": 4, "beverageType": "Vanilla Coffee", "brandName": "Dunkin®", "customStrength": "Strong", "customTemperature": "Hotter", "isDefault": False, "isRecommended": False, "varietyName": "Dunkin Decaf®"}, "dispenseSteps": [{"dispenseType": "Needle", "dispenseStepNumber": 0, "needleParameters": {"isEnhanced": False, "waterFlowrate": 12.5, "waterSource": "Hot Water", "waterTemperature": 198, "waterVolumePC": 95}}, {"dispenseType": "Powder", "dispenseStepNumber": 1, "powderParameters": {"frothDensity": "Medium", "frothRatioPC": 10, "powderMass": 5.0, "powderType": "Vanilla", "waterFlowrate": 12.5, "waterTemperature": 198, "waterVolumePC": 5}}, {"dispenseType": "Syrup", "dispenseStepNumber": 2, "syrupParameters": {"syrupType": "French Vanilla", "syrupVolume": 10}}, {"dispenseType": "Syrup", "dispenseStepNumber": 3, "syrupParameters": {"syrupType": "Vanilla", "syrupVolume": 10}}, {"dispenseType": "Syrup", "dispenseStepNumber": 4, "syrupParameters": {"syrupType": "Hazelnut", "syrupVolume": 10}}]}, "dispensed": {"startTime": "<utcTimestamp", "endTime": "utcTimestamp", "dispensedWater": [], "dispensedPowder": [], "dispensedFlavor": []}, "result": {"status": "<success|abort>", "info": {}}}})
    mqtt_manager.publish(TOPICS.IOT_AGENT_CONFIG_RELOAD,  "1")
    mqtt_manager.publish(TOPICS.AM_BREWSTART, str(start_brew_message))
    time.sleep(.01)
    mqtt_manager.publish(TOPICS.AM_BREWEND, str(end_brew_message))
    mqtt_manager.publish(TOPICS.IOT_AGENT_DB_TRANSMIT_BREWS,  "True")
    mqtt_manager.publish(TOPICS.IOT_AGENT_DB_TRANSMIT_PATCHES,  "True")


