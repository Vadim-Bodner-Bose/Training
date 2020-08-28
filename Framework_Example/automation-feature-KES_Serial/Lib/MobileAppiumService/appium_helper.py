import os

from appium import webdriver

# Returns abs path relative to this file and not cwd
from Config import MobileApp_Config
from Config.MobileApp_Config import iOS_CAPABILITIES, ANDROID_CAPABILITIES, APPIUM_SERVER_URL

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_android_dc(config):
    """ Android Appium desired capabilities.

    :deviceName: Unique device ID.
    :platformName: Mobile platform.
    :automationName: Name of Appium UI automation to be applied.
    :appPackage: Application package name.
    :appWaitActivity: Application activity name selected to be started with.
    :app Full path to application to be tested:
    :autoGrantPermissions: This permission for Android only, it grants all the possible permissions for application,
                           so you will never be asked to grant them during test.
    :noReset: Don't reset app state before this session
    :fullReset: Perform a complete reset.
    """
    return {
        "deviceName": config["ANDROID_DEVICE_NAME"],
        'platformName': "Android",
        "automationName": "UiAutomator2",
        # "appPackage": config["APP_PACKAGE"],
        # "appWaitActivity": config["APP_WAIT_ACTIVITY"],
        "app": PATH(config["ANDROID_APP_PATH"]),
        "autoGrantPermissions": True,
        # "noReset": True
        # "fullReset": True
    }


def get_ios_dc(config):
    """ iOS Appium desired capabilities.

    :deviceName: Name of your device.
    :platformName: Mobile platform.
    :automationName: Name of Appium UI automation to be applied.
    :udid: Unique ID of your device.
    :app Full path to application to be tested:
    :noReset: Don't reset app state before this session
    :fullReset: Perform a complete reset.
    :xcodeOrgId: Your developer member id
    :xcodeSigningId: Default text, see docs
    :bundleId: Bundle id of your application, using to run correct application on device
    :autoAcceptAlerts: Auto accept alerts to be thrown
    """
    return {
        "deviceName": config["IOS_DEVICE_NAME"],
        "udid": config["UUID"],
        'platformName': "iOS",
        "automationName": "XCUITest",
        "app": PATH(config["IOS_APP_PATH"]),
        # "noReset": True,
        # "fullReset": True,
        "xcodeOrgId": config["XCODE_ORG_ID"],
        "xcodeSigningId": config["XCODE_SIGNING_ID"],
        # "bundleId": config["BUNDLE_ID"],
        "autoAcceptAlerts": True
    }


def get_config(platform, config):
    """ Selection of config type based on platform type.
    At the beginning we have a lot of different arguments so we filter them with platform specific list of capabilities.

    :platform: Name of your device.
    :config: Pytest config containing all the parameters that help to create appium Desired Capabilities config.
    """
    if platform.lower() == 'Android'.lower():
        return get_android_dc(vars(config))
    elif platform.lower() == 'iOS'.lower():
        return get_ios_dc(vars(config))


def get_mobile_arguments(constants={}):
    """ Get all the mobile arguments to be able to receive appropriate arguments from command line.

    :constants: List of constants withdrawn from MobileApp_Config.
    """
    config_data = vars(MobileApp_Config)
    for key in config_data:
        if not key.startswith('__') and key != 'ANDROID_CAPABILITIES' and key != 'iOS_CAPABILITIES':
            constants[key] = config_data[key]
        elif key == 'ANDROID_CAPABILITIES' or key == 'iOS_CAPABILITIES':
            constants.update(config_data[key])
    return constants


class AppiumUtils:
    def __init__(self, desired_capabilities):
        """
        Class initialization

        :desired_capabilities: Appium desired capabilities.
        """
        self.driver = self.create_driver(desired_capabilities)

    @staticmethod
    def create_driver(desired_caps):
        """
        Create Appium driver to be able to run tests
        """
        driver = webdriver.Remote(APPIUM_SERVER_URL, desired_caps)
        return driver  # provide the fixture value
