from KWAD_Framework.base.DriverClass import Driver
import KWAD_Framework.utilities.CustomLogger as cl
from KWAD_Framework.base.BasePage import BasePage
from KWAD_Framework.pages.ContactUsForm import ContactForm

driver1 = Driver()
log = cl.customLogger()
driver = driver1.getDriverMethod()
log.info("Launching App")

cf = ContactForm(driver)

#cf.verifyContactPage()
cf.clickContactFormButton()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterMNumber()
cf.clickSubmitButton()