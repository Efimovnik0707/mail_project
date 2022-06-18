import time
from .pages.locators import MainPageLocators
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.mail_page import MailPage
from selenium.webdriver.common.by import By
import pytest

class TestUserCanSendMail():
    @pytest.fixture(scope="function", autouse=True)
    def test_guest_can_login(self, browser):
        self.link = "https://login.aol.com/?src=fp-uk&client_id=LFiURcyscrEXmciV&crumb=&intl=uk&redirect_uri=https%3A%2F%2Foidc.www.aol.co.uk%2Fcallback&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3DLFiURcyscrEXmciV%26intl%3Duk%26nonce%3Dp6iJMegcza6uieXHQ9HupVeNmlug3Evb%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.co.uk%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-uk%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jby51ay8ifQ.orGlPndYGcsOZdfcdF-8AOZnHNoS6mu9V4kGxkKtyrQAsrkmQPgowubTCTxF0ih_FmPPuVqFj8I60PlYHdIFTv_OJbZx5GyfsaWp7k1P79GZcfWDMB59nm0NSHt0Dp3bUx1flHJNFVpp8SxDcCp7_VLZywEnAaKrR1O_gKe6f88"
        self.page = LoginPage(browser, self.link)
        self.page.open()
        self.page.user_login()
    

    def test_user_send_read_delete(self, browser):
        self.link = "https://mail.aol.com/webmail-std/en-gb/suite"
        self.page = MailPage(browser, self.link)
        self.page.open()
        self.page.run_mail(2) # in () enter the number of mails to be sent


    
