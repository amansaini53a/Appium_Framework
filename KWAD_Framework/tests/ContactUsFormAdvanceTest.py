import unittest,pytest
from KWAD_Framework.pages.ContactUsForm import ContactForm

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse= True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=1)
    def test_openContactForm(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()
