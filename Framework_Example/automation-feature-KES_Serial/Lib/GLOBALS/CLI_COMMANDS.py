"""
This file houses all CLI commands for all brewers
"""

####################
# Generic Arenal/Krakatoa CLI COMMANDS
####################


POWER_ON = "POWER ON"
POWER_OFF = "POWER OFF"
PRINT_BE_ON = "PRINT_BE ON"
PRINT_BE_OFF = "PRINT_BE OFF"
VERBOSE_ON = "VERBOSE ON"
VERBOSE_OFF = "VERBOSE OFF"
VERBOSE_PROBE_ON = "VERBOSE PROBE ON"
VERBOSE_PROBE_OFF = "VERBOSE PROBE OFF"
PRINT_HRT_ON = "PRINT_HRT ON"
PRINT_HRT_OFF = "PRINT_HRT OFF"
TEST_MODE_ON = "TEST_MODE ON"
TEST_MODE_OFF = "TEST_MODE OFF"
HIGH_ALT_ON = "HIGH_ALT ON"
HIGH_ALT_OFF = "HIGH_ALT OFF"
TEMP_OFFSET = "TEMP_OFFSET"
PREHEAT_TEMP = "PREHEAT_TEMP"
BREW_TYPE_NORMAL = "BREW_TYPE N"
BREW_TEMP_194 = "BREW_TEMP 19400"
RECIPE_SIZE_4OZ = "RECIPE_SIZE 4"
RECIPE_4OZ_ROBUST_HIGH = "RECIPE 4, 7383, 1000"
START_BREW = "START_BREW"
AUTO_BREW = "AUTO-BREW 3, 5, 4"
EEPROM_PRINT = "EEPROM_PRINT"
RESET = "RESET"
FVT_MODE = "?????????"
DISPENSE_MAX_PRESSURE = "DISPENSE_MAX_PRESSURE"
DISPENSE_AVG_PRESSURE = "DISPENSE_AVG_PRESSURE"
SIM_BREW_STATUS = "SIM_BREW_STATUS"
SIM_BREW_ERROR = "SIM_BREW_ERROR"

####################
# Additional KES Krakatoa CLI COMMANDS
####################


KES_FACTORY_RESET = "FACTORY_RESET"
KES_INITIAL_AIRPUMP_PWM = "INITIAL_AIRPUMP_PWM"
KES_FINAL_AIRPUMP_PWM = "FINAL_AIRPUMP_PWM"
KES_STRONG_INITIAL_AIRPUMP_PWM = "STRONG_INITIAL_AIRPUMP_PWM"
KES_STRONG_FINAL_AIRPUMP_PWM = "STRONG_FINAL_AIRPUMP_PWM"
KES_AIRPUMP_INCREASE_TIME = "AIRPUMP_INCREASE_TIME"
KES_AIRPUMP_INCREASE_TIMER = "AIRPUMP_INCREASE_TIMER"
KES_PURGE_RECOVERY_TIME = "PURGE_RECOVERY_TIME"
KES_PURGE_TIMEOUT = "PURGE_TIMEOUT"
KES_BELOW_PRESSURE = "BELOW_PRESSURE"
KES_STRONG_PURGE_TIME = "STRONG_PURGE_TIME"
KES_STRONG_PURGE_TIMEOUT = "STRONG_PURGE_TIMEOUT"
KES_STRONG_PURGE_TOGGLE_TIMER = "STRONG_PURGE_TOGGLE_TIMER"
KES_STRONG_PURGE_RAMPUP = "STRONG_PURGE_RAMPUP"
KES_MIN_PURGE_TIME = "MIN_PURGE_TIME"
KES_GET_MAINT_DATA = "GET_MAINT_DATA"
KES_SW_VERSION = "SW_VERSION"
KES_CANCEL_BREW = "CANCEL_BREW"
KES_SIM_CWT_REMOVAL = "SIM_CWT_REMOVAL"
KES_PM_OPEN = "PM OPEN"
KES_PM_CLOSE = "PM CLOSE"
KES_BE_STATE = "BE_STATE"

KES_RECIPE_160_75_4 = "RECIPE 160 7.5 4"
KES_RECIPE_187_75_4 = "RECIPE 187 7.5 4"
KES_RECIPE_191_75_4 = "RECIPE 191 7.5 4"
KES_RECIPE_194_75_4 = "RECIPE 194 7.5 4"
KES_RECIPE_196_75_4 = "RECIPE 196 7.5 4"
KES_RECIPE_200_75_4 = "RECIPE 200 7.5 4"
KES_RECIPE_204_75_4 = "RECIPE 204 7.5 4"

KES_RECIPE_194_75_6 = "RECIPE 194 7.5 6"
KES_RECIPE_194_75_8 = "RECIPE 194 7.5 8"
KES_RECIPE_194_75_10 = "RECIPE 194 7.5 10"
KES_RECIPE_194_75_12 = "RECIPE 194 7.5 12"

KES_SETUP_WIFI = "SETUP_WIFI"
KES_ABORT_WIFI_SETUP = "ABORT_WIFI_SETUP"
KES_FORGET_WIFI = "FORGET_WIFI"
####################
# Additional Premium Arenal CLI COMMANDS
####################


PRE_FACTORY_RESET = "FACTORY_RESET"
PRE_INITIAL_AIRPUMP_PWM = "INITIAL_AIRPUMP_PWM"
PRE_FINAL_AIRPUMP_PWM = "FINAL_AIRPUMP_PWM"
PRE_STRONG_INITIAL_AIRPUMP_PWM = "STRONG_INITIAL_AIRPUMP_PWM"
PRE_STRONG_FINAL_AIRPUMP_PWM = "STRONG_FINAL_AIRPUMP_PWM"
PRE_AIRPUMP_INCREASE_TIME = "AIRPUMP_INCREASE_TIME"
PRE_AIRPUMP_INCREASE_TIMER = "AIRPUMP_INCREASE_TIMER"
PRE_PURGE_RECOVERY_TIME = "PURGE_RECOVERY_TIME"
PRE_PURGE_TIMEOUT = "PURGE_TIMEOUT"
PRE_BELOW_PRESSURE = "BELOW_PRESSURE"
PRE_STRONG_PURGE_TIME = "STRONG_PURGE_TIME"
PRE_STRONG_PURGE_TIMEOUT = "STRONG_PURGE_TIMEOUT"
PRE_STRONG_PURGE_TOGGLE_TIMER = "STRONG_PURGE_TOGGLE_TIMER"
PRE_STRONG_PURGE_RAMPUP = "STRONG_PURGE_RAMPUP"
PRE_MIN_PURGE_TIME = "MIN_PURGE_TIME"
PRE_GET_MAINT_DATA = "GET_MAINT_DATA"
PRE_INDIRECT_PRESSURE_PWM = "INDIRECT_PRESSURE_PWM"
PRE_INDIRECT_PRESSURE_TIME = "INDIRECT_PRESSURE_TIME"
PRE_MUG_SENSOR = "MUG_SENSOR"
PRE_BOOT_MODE = "BOOT_MODE"
PRE_SWUP = "SWUP"

####################
# Premium Ayla Connectivity CLI COMMANDS, AL - stand for Ayla
####################

AL_CURRENT_WIFI_STATUS = "show wifi"
AL_ENABLE_ACTIVE_PROFILE = "wifi profile enable"
AL_ERASE_ACTIVE_PROFILE = "wifi profile erase"
AL_RESET_WIFI_MODULE = "reset"
AL_SAVE_CONFIGURATION = "save"
AL_SET_ACTIVE_PROFILE_0 = "wifi profile 0"
AL_TURN_OFF_WIFI = "wifi disable"
AL_TURN_ON_WIFI = "wifi enable"

####################
# Premium Sandstone Connectivity CLI COMMANDS, SS - stnds for Sandstone
####################
SS_RESET = "RESET"