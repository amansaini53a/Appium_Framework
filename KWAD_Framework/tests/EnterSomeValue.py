from KWAD_Framework.base.DriverClass import Driver
import KWAD_Framework.utilities.CustomLogger as cl
from KWAD_Framework.base.BasePage import BasePage
from KWAD_Framework.pages.EnterValuePage import EnterValue

driver1 = Driver()
log = cl.customLogger()
driver = driver1.getDriverMethod()
log.info("Launching App")

cf = EnterValue(driver)

#cf.verifyContactPage()
cf.clickEnterValue()
cf.sendValue()
cf.clickSubmitButton()



# bp.screenShot("App")
# bp = BasePage(driver)
# element = bp.waitForElement("com.code2lead.kwad:id/EnterValue", "id")
# element.click()
# element = bp.isDisplayed("com.code2lead.kwad:id/EnterValue", "id")
# print(element)
# bp.clickElement("com.code2lead.kwad:id/EnterValue", "id")
# bp.screenShot("Enter Value")
#bp.sendText()