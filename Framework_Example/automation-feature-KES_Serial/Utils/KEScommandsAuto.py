from Lib.SerialConnection import SerialConnection as sc
import time
from Lib.SerialConnection import SerialConnection


# dictionary format: command:{optional parameters<may be also a dictionary>,response, delay, skip}
# check params for the RECIPE command
brewer_command_dict = {'VERBOSE': ('VERBOSE', 0.2, 'RUN'), 'VERBOSE PROBE': ('VERBOSE', 0.1, 'RUN'),
                       'TEST_MODE': ('TEST MODE', 0.1, 'RUN'), 'POWER': ('POWER', 0.1, 'RUN'),
                       'RECIPE_SIZE': ('RECIPE SIZE', 0.1, 'RUN'),
                       'START_BREW': ('START', 0.5, 'SKIP'), 'RESET': ('RESET', 5, 'SKIP'),
                       'RECIPE': ('RECIPE', 0.1, 'SKIP'),
                       'BREW_TEMP': ('Default brew temperature', 0.1, 'RUN'),
                       'TEMP_OFFSET': ('Default temperature offset', 0.1, 'RUN'),
                       'PREHEAT_TEMP': ('Default preheat temperature', 0.1, 'RUN'),
                       'HIGH_ALT': ('High Altitude', 0.1, 'RUN'),
                       'FACTORY_RESET': ('Factory Reset requested', 1, 'RUN'),
                       'PANAMA': ('PANAMA', 0.1, 'SKIP'),
                       'INITIAL_AIRPUMP_PWM': ('INITIAL AIR PUMP PWM', 0.1, 'RUN'),
                       'FINAL_AIRPUMP_PWM': ('FINAL AIR PUMP PWM', 0.1, 'RUN'),
                       'STRONG_INITIAL_AIRPUMP_PWM': ('STRONG INITIAL AIR PUMP PWM', 0.1, 'RUN'),
                       'STRONG_FINAL_AIRPUMP_PWM': ('STRONG FINAL AIR PUMP PWM', 0.1, 'RUN'),
                       'AIRPUMP_INCREASE_TIME': ('AIR PUMP INCREASE TIME', 0.1, 'RUN'),
                       'AIRPUMP_INCREASE_TIMER': ('AIR PUMP INCREASE TIMER', 0.1, 'RUN'),
                       'PURGE_RECOVERY_TIME': ('PURGE RECOVERY TIME', 0.1, 'RUN'),
                       'PURGE_TIMEOUT': ('PURGE TIMEOUT', 0.1, 'RUN'),
                       'BELOW_PRESSURE': ('BELOW PRESSURE', 0.1, 'RUN'),
                       'STRONG_PURGE_TIME': ('STRONG PURGE TIME', 0.1, 'RUN'),
                       'STRONG_PURGE_TIMEOUT': ('STRONG PURGE TIMEOUT', 0.1, 'RUN'),
                       'STRONG_PURGE_TOGGLE_TIMER': ('STRONG PURGE TOGGLE TIMER', 0.1, 'RUN'),
                       'STRONG_PURGE_RAMPUP': ('STRONG PURGE RAMPUP TIME', 0.1, 'RUN'),
                       'MIN_PURGE_TIME': ('MINIMUM PURGE TIME', 0.1, 'RUN'),
                       'DISPENSE_MAX_PRESSURE': ('Max dispense pressure', 0.1, 'RUN'),
                       'DISPENSE_AVG_PRESSURE': ('Average dispense pressure', 0.1, 'RUN'),
                       'GET_MAINT_DATA': ('MAIN', 8, 'RUN'),
                       'IDP_PURGE_PWM_COEFFICIENT': ('IDP', 0.1, 'RUN'),
                       'IDP_PURGE_PWM_EXPONENT': ('IDP', 0.1, 'RUN'),
                       'IDP_PURGE_DELAY_COEFFICIENT': ('IDP', 0.1, 'RUN'),
                       'IDP_PURGE_DELAY_EXPONENT': ('', 0.1, 'RUN'),
                       'IDP_PURGE_RAMP_INCREMENT': ('IDP', 0.1, 'RUN'),
                       'BIT_LEDS': ('BIT', 0.1, 'RUN'),
                       '????????': ('TESTMODE', 0.1, 'RUN')}
# init response dictionary
command_response = {}
global serial
serial = SerialConnection()
serial.establish_connection()
time.sleep(1)


for cmd, cfg in brewer_command_dict.items():
    # for cfg in cmd:
    # check if the command returns proper response now
    # if the config dictionary says 'SKIP' command doesn't execute.
    if cfg[2] == 'RUN':
        response = serial.send_receive_data(cmd, cfg[0])
        time.sleep(cfg[1])
        # populate a new dict with the used command and response pass/fail
        command_response.update(dict({cmd: response}))
    else:
        pass

print("list of commands and response states {}".format(command_response))
