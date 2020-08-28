"""
This file contains all MQTT TOPICS
"""

################################
# Appliance Manager Topics
################################

AM_WORKFLOWID = "appliance/v0.1/ApplianceManager/Input/Workflow/WorkflowId"
AM_WORKFLOW_BREWTYPE = "appliance/v0.1/ApplianceManager/Input/Workflow/BrewType"
AM_DISPENSEORDER = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/DispenseOrder"
AM_WORKFLOW_PCTVOLUME = "appliance/v0.1/ApplianceManager/Input/Workflow/BE/PercentageVolume"
AM_WORKFLOW_BE_TOTALVOLUMEML = "appliance/v0.1/ApplianceManager/Input/Workflow/BE/TotalVolumeML"
AM_WORKFLOW_BE_BREWTEMPCELSIUS = "appliance/v0.1/ApplianceManager/Input/Workflow/BE/BrewTemperatureC"
AM_WORKFLOW_BE_FLOWRATEMLM = "appliance/v0.1/ApplianceManager/Input/Workflow/BE/FlowRateMLM"
AM_WORKFLOW_BE_HWTTEMPCELSIUS = "appliance/v0.1/ApplianceManager/Input/Workflow/BE/HWTTemperatureC"
AM_WORKFLOW_BE_AIRPURGETIMEMS = "appliance/v0.1/ApplianceManager/Input/Workflow/BE/AirPurgeTimeMS"
AM_WORKFLOW_POWDER_1_ENABLE = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Enable"
AM_WORKFLOW_POWDER_1_AIRPURGETIMEMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/AirPurgeTimeMS"
AM_WORKFLOW_POWDER_1_FLOWMLM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/FlowRateMLM"
AM_WORKFLOW_POWDER_1_FLOWMGM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/FlowRateMGM"
AM_WORKFLOW_POWDER_1_PCTVOL = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/PercentageVolume"
AM_WORKFLOW_POWDER_1_VOLMG = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/VolumeMG"
AM_WORKFLOW_POWDER_1_BREWTEMPC = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/BrewTemperatureC"
AM_WORKFLOW_POWDER_1_WHIP_FROTHRATIO = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/FrothRatio"
AM_WORKFLOW_POWDER_1_WHIP_FROTHDENSTIY = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/FrothDensity"
AM_WORKFLOW_POWDER_2_FLOWMLM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/FlowRateMLM"
AM_WORKFLOW_POWDER_2_FLOWMGM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/FlowRateMGM"
AM_WORKFLOW_POWDER_1_AUGER_TSTARTMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Auger/TStartMS"
AM_WORKFLOW_POWDER_1_AUGER_TDURATIONMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Auger/TDurationMS"
AM_WORKFLOW_POWDER_1_AUGER_PWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Auger/PWM"
AM_WORKFLOW_POWDER_2_ENABLE = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Enable"
AM_WORKFLOW_POWDER_2_AIRPURGETIME = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/AirPurgeTimeMS"
AM_WORKFLOW_POWDER_2_PCTVOL = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/PercentageVolume"
AM_WORKFLOW_POWDER_2_VOLMG = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/VolumeMG"
AM_WORKFLOW_POWDER_2_BREWTEMPC = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/BrewTemperatureC"
AM_WORKFLOW_POWDER_2_WHIP_FROTHRATIO = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/FrothRatio"
AM_WORKFLOW_POWDER_2_WHIP_FROTHDENSTIY = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/FrothDensity"
AM_WORKFLOW_FAN_ONOFF = "appliance/v0.1/ApplianceManager/Input/Workflow/Fan/OnOff"
AM_WORKFLOW_FAN_IDLESPEEDPWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Fan/IdleSpeedPWM"
AM_WORKFLOW_FAN_DISPENSESPEEDPWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Fan/DispenseSpeedPWM"
AM_BREWSTART = "appliance/v0.1/ApplianceManager/Workflow/BrewStart"
AM_BREWCANCEL = "appliance/v0.1/ApplianceManager/Input/BrewCancel"
AM_BREWEND = "appliance/v0.1/ApplianceManager/Workflow/BrewEnd"

# AM_WORKFLOW_BEVERAGEPOWDERRATIO = "appliance/v0.1/ApplianceManager/Input/Workflow/BeveragePowderRatio"
# AM_WORKFLOW_POWDER_2_WHIPPER_TSTARTMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/TStartMS"
# AM_WORKFLOW_POWDER_2_WHIPPER_TDURATIONMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/TDurationMS"
# AM_WORKFLOW_POWDER_2_WHIPPER_MIXRATIO = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/MixRatio"
# AM_WORKFLOW_POWDER_2_WHIPPER_MIXPM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/MixPWM"
# AM_WORKFLOW_POWDER_2_WHIPPER_FROTHPWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Whipper/FrothPWM"
# AM_WORKFLOW_POWDER_2_AUGER_TSTARTMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Auger/TStartMS"
# AM_WORKFLOW_POWDER_2_AUGER_TDURATIONMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Auger/TDurationMS"
# AM_WORKFLOW_POWDER_2_AUGER_PWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/2/Auger/PWM"
# AM_WORKFLOW_POWDER_1_WHIPPER_TSTARTMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/TStartMS"
# AM_WORKFLOW_POWDER_1_WHIPPER_TDURATIONMS = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/TDurationMS"
# AM_WORKFLOW_POWDER_1_WHIPPER_MIXRATIO = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/MixRatio"
# AM_WORKFLOW_POWDER_1_WHIPPER_MIXPWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/MixPWM"
# AM_WORKFLOW_POWDER_1_WHIPPER_FROTHPWM = "appliance/v0.1/ApplianceManager/Input/Workflow/Powder/1/Whipper/FrothPWM"


########################
# BrewEngineProxy Topics
########################


BEP_REQUESTALLVALUES = "appliance/v0.1/BrewEngineProxy/Inputs/requestAllValues_"
BEP_HIGHALTITUDEENABLED = "appliance/v0.1/BrewEngineProxy/Inputs/highAltitudeEnabled_"
BEP_PREHEATTEMPFRNHT = "appliance/v0.1/BrewEngineProxy/Inputs/preheatTempInHundredthsDegF_"
BEP_BREWSIZEOZ = "appliance/v0.1/BrewEngineProxy/Inputs/brewSizeInOz_"
BEP_BREWSIZEMICROLITERS = "appliance/v0.1/BrewEngineProxy/Inputs/brewSizeMicroliters_"
BEP_BREWFLOWRATEULPERSEC = "appliance/v0.1/BrewEngineProxy/Inputs/brewFlowRateUlPerSec_"
BEP_BREWTEMPFRNHT = "appliance/v0.1/BrewEngineProxy/Inputs/brewTempInHundredthsDegF_"
BEP_BREWTEMPOFFSETFRNHT = "appliance/v0.1/BrewEngineProxy/Inputs/brewTempOffsetInHundredthsDegF_"
BEP_WATERPUMPINITPWM = "appliance/v0.1/BrewEngineProxy/Inputs/waterPumpInitialPwm_"
BEP_UPDATERECIPEREQUEST = "appliance/v0.1/BrewEngineProxy/Inputs/updateRecipeRequest_"
BEP_STARTBREW = "appliance/v0.1/BrewEngineProxy/Inputs/startBrew_"
BEP_BREWTYPE = "appliance/v0.1/BrewEngineProxy/Inputs/brewType_"
BEP_CANCELBREW = "appliance/v0.1/BrewEngineProxy/Inputs/cancelBrew_"
BEP_VERBOSEMODE = "appliance/v0.1/BrewEngineProxy/Inputs/verboseMode_"
BEP_BITTEST = "appliance/v0.1/BrewEngineProxy/Inputs/bitTest_"
BEP_BITTESTCOMMAND = "appliance/v0.1/BrewEngineProxy/Inputs/bitTestCommand_"
BEP_FACTORYRESET = "appliance/v0.1/BrewEngineProxy/Inputs/factoryReset_"
BEP_ENABLEMEDUSAPM = "appliance/v0.1/BrewEngineProxy/Inputs/enableMedusaPm_"
BEP_REQMAINTSTATE = "appliance/v0.1/BrewEngineProxy/Inputs/reqMaintState_"
BEP_EXITMAINTSTATE = "appliance/v0.1/BrewEngineProxy/Inputs/exitMaintState_"
BEP_SUVERSION = "appliance/v0.1/BrewEngineProxy/Inputs/suVersion_"
BEP_SUSIZE = "appliance/v0.1/BrewEngineProxy/Inputs/suSize_"
BEP_SUCHECKSUM = "appliance/v0.1/BrewEngineProxy/Inputs/suChecksum_"
BEP_SUDATABLOCK = "appliance/v0.1/BrewEngineProxy/Inputs/suDataBlock_"
BEP_HWTEMPFRNT = "appliance/v0.1/BrewEngineProxy/Inputs/hwtTempInHundrethsDegF_"
BEP_RESETMAINBOARD = "appliance/v0.1/BrewEngineProxy/Inputs/resetMainBoard_"
BEP_STARTRINSE = "appliance/v0.1/BrewEngineProxy/Inputs/startRinse_"
BEP_POWERSTATE = "appliance/v0.1/BrewEngineProxy/Inputs/powerState_"
BEP_SETBREWTEMPFRNHT = "appliance/v0.1/BrewEngineProxy/Inputs/setBrewTempHundDegF_"
BEP_PREHEATTEMP_FRNHT_ = "appliance/v0.1/BrewEngineProxy/Inputs/preheatTempHundDegF_"
BEP_SUTRANSFERSTATE = "appliance/v0.1/BrewEngineProxy/Inputs/suTransferState_"
BEP_SUAPPLYSTATE = "appliance/v0.1/BrewEngineProxy/Inputs/suApplyState_"
BEP_BREWCANCELREASON = "appliance/v0.1/BrewEngineProxy/Inputs/brewCancelReason_"
BEP_WORKFLOW = "appliance/v0.1/BrewEngineProxy/Input/Workflow"

#######################
# Powder Dispense Proxy
#######################

POWDER_DISPENSE_PROXY_SUBSCRIBE = ["appliance/v0.1/ApplianceManager/Internal/powderDispenseComplete",
                                   "appliance/v0.1/PowderDispenseProxy/Input/12/powderFlowRate",
                                   "appliance/v0.1/PowderDispenseProxy/Input/1/whipSetting",
                                   "appliance/v0.1/PowderDispenseProxy/Input/13/powderFlowRate",
                                   "appliance/v0.1/PowderDispenseProxy/Input/3/whipSetting",
                                   "appliance/v0.1/PowderDispenseProxy/Input/13/targetEncoderRevolutions",
                                   "appliance/v0.1/PowderDispenseProxy/Input/1/value",
                                   "appliance/v0.1/PowderDispenseProxy/Input/2/value",
                                   "appliance/v0.1/PowderDispenseProxy/Input/12/targetEncoderRevolutions",
                                   "brewerSync/sandstone/brewer/outputs/workflowState_",
                                   "appliance/v0.1/PowderDispenseProxy/Output/0/encoderRevsReached",
                                   "appliance/v0.1/PowderDispenseProxy/Output/2/encoderRevsReached",
                                   "brewerSync/sandstone/brewer/outputs/brewEngineState_",
                                   "brewerSync/sandstone/brewer/outputs/brewStatus_", "#"]

PWD_DISP_PRXY_OUT_0_ENCODER_REV = "appliance/v0.1/PowderDispenseProxy/Output/0/encoderRevsReached"
PWD_DISP_PRXY_OUT_2_ENCODER_REV = "appliance/v0.1/PowderDispenseProxy/Output/2/encoderRevsReached"
BREWER_SYNC_WORKFLOW_STATE = "brewerSync/sandstone/brewer/outputs/workflowState_"


##################
# IOT Agent Topics
##################

IOT_AGENT_CONFIG_RELOAD = "appliance/v0.1/IoTAgent/Configuration/Reload"
IOT_AGENT_DB_TRANSMIT_BREWS = "appliance/v0.1/IoTAgent/Database/Transmit/Brews"
IOT_AGENT_DB_TRANSMIT_PATCHES = "appliance/v0.1/IoTAgent/Database/Transmit/Patches"
