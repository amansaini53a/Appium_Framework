from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'CPH1823'
        desired_caps['app'] = 'D:\Python_Pycharm\Appium_framework\KWAD_Framework\_apk\Android_Demo_App.apk'
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return driver

