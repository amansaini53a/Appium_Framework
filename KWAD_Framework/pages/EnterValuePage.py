from KWAD_Framework.base.BasePage import BasePage


class EnterValue(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        #Locators vallue in Enter Some Value
    _enterValueButton = "com.code2lead.kwad:id/EnterValue"      #id
    _pageTitle = "Enter some Value"                             #text
    _sendValue = "android.widget.EditText"                              #
    _clickSubmit = "com.code2lead.kwad:id/Btn1"                 #id

    def clickEnterValue(self):
        self.clickElement(self._enterValueButton,"id")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle,"text")
        assert element == False

    def sendValue(self):
        self.sendText("AmanSaini",self._sendValue,"class")

    def clickSubmitButton(self):
        self.clickElement(self._clickSubmit,"id")