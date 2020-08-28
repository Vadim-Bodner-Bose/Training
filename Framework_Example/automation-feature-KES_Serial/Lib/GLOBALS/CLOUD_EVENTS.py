# Ayla Events
AYLA_STATUS_BREW = "BREW"
AYLA_STATUS_IN_PROGRESS = "BREW_IN_PROGRESS"
AYLA_STATUS_CANCELLED = "BREW_CANCELLED"
AYLA_STATUS_IDLE = "IDLE"
AYLA_STATUS_STANDBY = "STANDBY"
AYLA_STATUS_SUCCESSFUL = "BREW_SUCCESSFUL"
AYLA_SOURCE = "MOBILE-APP"
AYLA_OTA_LOG = "Software Update: apply passed"
AYLA_DEVICE_ON = "Online"
AYLA_DEVICE_OFF = "Offline"
AYLA_REQ_RECIPE = {"size": 8, "brew_type": "HOT_WATER", "flow_rate": 7390, "temp": 194, "enhanced": False,
                   "recipe_category": "WATER"}
AYLA_STATE_MODE_BREW = {"current": "BREW", "change_cause": "REMOTE_BREW_REQUEST", "req_source": "MOBILE-APP",
                        "brew_lock_causes": "PM_NOT_CYCLED", "req_id": None}
AYLA_STATE_MODE_BREW_IDLE = {"current": "IDLE", "change_cause": "BREW_COMPLETE_IDLE_REQUEST",
                             "req_source": "MOBILE-APP", "req_id":None, "brew_lock_causes": "PM_NOT_CYCLED"}
AYLA_STATE_MODE_REQ_IDLE = {"current": "IDLE", "change_cause": "REMOTE_IDLE_REQUEST", "req_source": "MOBILE-APP",
                            "req_id": None}
AYLA_STATE_MODE_REQ_STANDBY = {"current": "STANDBY", "change_cause": "REMOTE_STANDBY_REQUEST",
                               "req_source": "MOBILE-APP", "req_id": None}

# Azure Twin parts
AZURE_OTA_SUCCESS = {'phase': 'COMPLETE-NO-ERR', 'percent': 100, 'errCode': 0}