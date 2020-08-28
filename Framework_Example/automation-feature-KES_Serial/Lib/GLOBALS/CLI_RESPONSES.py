"""
This file houses all CLI responses for all brewers
"""

####################
# Premium Arenal CLI Responses
####################
PRE_BE_STATE_STANDBY = "BE state STANDBY"
PRE_BE_STATE_IDLE = "BE state IDLE"
PRE_BREW_COMPLETE = "BA state BREW_COMPLETE"
PRE_BREWING = "BA state BREWING"
PRE_BE_LOGGING_ON = "PRINT_BE is ON"
PRE_BE_POWER_STATE_OFF = "POWER state is OFF"

####################
# Premium Ayla Connectivity CLI Responses, AL - stand for Ayla
####################
AL_ACK = '-->'
AL_CONFIGURATION_SAVED = "configuration saved"
# replace with the wifi network you are expecting to be connected by using AL_WIFI_PROFILE.format(wifi_network)
AL_WIFI_PROFILE = "0            {}"

####################
# Premium Sandstone Connectivity CLI Responses, SS - stnds for Sandstone
####################
SS_RESET = "MAIN PCB"

####################
# KES Krakatoa CLI Responses
####################
KES_POWER_IS_ON = "POWER state is ON"
KES_POWER_IS_OFF = "POWER state is OFF"
KES_PRINT_BE_IS_ON = "PRINT_BE ON"
KES_PRINT_BE_IS_OFF = "PRINT_BE OFF"
KES_VERBOSE_IS_ON = "VERBOSE is ON"
KES_VERBOSE_IS_OFF = "VERBOSE is OFF"
KES_SUCCESSFUL_BREW = "BREW_SUCCESSFUL"
KES_UNSUCCESSFUL_BREW = "BREW_UNSUCCESSFUL"
KES_BREW_CANCELLING = "BREW_CANCELLING"
KES_BREW_CANCELLED = "BREW_CANCELLED"
KES_BE_STATE_IDLE = "BE State = IDLE"
KES_BE_STATE_STANDBY = "BE State = STANDBY"
KES_160_TEMP = "Custom Recipe: 16000 F"
KES_187_TEMP = "Custom Recipe: 18700 F"
KES_191_TEMP = "Custom Recipe: 19100 F"
KES_194_TEMP = "Custom Recipe: 19400 F"
KES_196_TEMP = "Custom Recipe: 19600 F"
KES_200_TEMP = "Custom Recipe: 20000 F"
KES_204_TEMP = "Custom Recipe: 20400 F"