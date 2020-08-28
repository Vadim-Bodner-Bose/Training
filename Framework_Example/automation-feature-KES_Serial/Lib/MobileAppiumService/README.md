Mobile service
==============

This service is aimed to cover testing of Mobile application, including Appium and Mobile application features


How to run Appium tests
-------------

**List of the tools to be installed**

----Android-Windows----
* Appium version 1.15.1
* Android Studio 3.5.3 (add to env variables)
* Java SKD version 1.8.0_241 (add to env variables)
* Node.js version 12.16.1 (npm 6.13.4) - need to support Appuim
* Appium Doctor v.1.14.0
* Python 3.8 -> (to run test framework)
* PyCharm Community Edition -> (to run test framework) 
* plug device and check adb devices 

```shell
To fix issue of Appium with UiAutomator2, follow instructions
===================================================
1. Make sure appium server is not executing.
2. Connect your android device with USB, also verify that device is connected properly by using command: adb devices
3. Execute below commands:
    adb uninstall io.appium.uiautomator2.server
    adb uninstall io.appium.uiautomator2.server.test
4. Start appium server
5. Start executing appium test cases
```

after all check that appium has all the dependant tools -> appium-doctor android
  
----iOS-Android-Mac----
* Appium version 1.15.1
* Homebrew
* Node JS v12.16.2 (npm 6.14.4) -> node -v -> npm -v
* Xcode 11.3.1
* Command line tools for Xcode 11.3.1
* Java JDK version 1.8.0_251 (setup JAVA_HOME and bin directory) -> java -version -> echo $JAVA_HOME
* Carthage 0.33.0
* Appium Doctor 1.15.1 -> (npm install appium-doctor -g)
* PyCharm Community Edition -> (to run test framework)
* Android Studio 3.5.3 (add to env variables)
* PyEnv 1.2.18 (to run python virtual env) -> brew install pyenv - pyenv install 3.8.2 -> pyenv version
* Python 3.8.2
* plug device and check "adb devices" or "instruments -s devices"


```shell
Set JAVA_HOME and ANDROID_HOME in the .bash_profile file.
===================================================
Navigate to home directory: cd ~/
Open bash profile file: open -e .bash_profile
Create bash profile: touch .bash_profile

export JAVA_HOME=$(/usr/libexec/java_home)
export ANDROID_HOME=${HOME}/Library/Android/sdk

export PATH="${JAVA_HOME}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}"

Apply changes: Source .bash_profile
Echo $JAVA_HOME
Echo $ANDROID_HOME
```

```shell
Register your device in Apple
===================================================
Before all - ask Oleksiy SLavutskyy or Maksim Yermachonok to clarify if this article is still valid
Aks Phil Headly to regidter you Apple device
To be registered as part of Keurig Apple team you need:
- Apple id registered to your corporate email
- devide uuid, if any

Steps to be done:
    1) login to developer.apple.com
    2) navigate to https://developer.apple.com/account/resources/certificates/list
    3) click the plus "+"
    4) select "iOS App Development" and click "Continue"
    5) follow instructions to create a CSR file and upload it
    6) download your developer certificate and double-click it on your Mac to install it into your keychain
    7) let Phil Headly know when this is complete, and then he'll add your new developer certificate to our app's provisioning profile.  I'll send you the new .mobileprovision file that you can use to sign the app on your box.
```

```shell
Setup Appium WebdriverAgent.
===================================================
Create Apple id and ask your team lead to give you developer team sertificate
Navigate to home directory: cd Applications/Appium.app/Contents/Resources/app/node_modules/appium-webdriveragent 
Then enter command: open .
When folder is opened double click: WebDriverAgent.xcodeproj
Now project is opened in Xcode
Go to WebDriverAgentRunner -> Signing and Capabilities
For "Team" add appropriate APPLE ID (in iCloud) and login in it
Select "Keurig Green Mountain, Inc" as your team
Change "Bundle identifier" to "com.keurig.kconnectent"
Try to build any simulator -> Biuld success
Ensure there is no warnings
```

```shell
Setup Appium WebdriverAgent.
===================================================
TODO: Create mobile app signed with Keurig certifacate
Install it to Mobile device tested
Trust the app for this device.
So it will e possible to uninstall tested app and install it back without manual trust for app installed 
```

```shell
Need iOS 13.4 support in XCode 11.3.1 ?
===================================================
You updated your iPhone iOS to 13.4 ?
You don't want to upgrade your OSX to Catalina in order to get the latest XCode 11.4?
Download the XCode release that does support your device from here: https://developer.apple.com/download/more
Extract the zip file, right click on Xcode.app, click on "Show Package Contents"
Go into folder: Contents -> Developer -> Platforms -> iPhoneOS.platform -> DeviceSupport
Find your iOS version you need support for and copy that folder to your existing Xcode.app within the same folder.
DONE.

This process will work for new and old versions of iOS & XCode.
```

after all:
- check that appium has all the dependant tools -> appium-doctor

**List of libraries**
* pip install -U pytest
* pip install Appium-Python-Client
* brew install pyenv

Variables to run tests
-------------

* Device mark e.g. "Samsung X"
* Version of OS e.g. "Android 10"
* Application version/build e.g. "Version 1.2.1 (2031)"
* Environment e.g. "REG"
* PROD/NonPROD e.g. "NonPROD"
* Commercial/NonCommercial e.g. "NonCommercial"
