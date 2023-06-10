import time
from Utility.Logger import Logging
from PageObjects.LoginPage import LoginPage
from Utility.readConfig import ReadConfig

class TestLogin:

    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = Logging.logGen()

    def test_PageTitle_001(self , setup):
        self.log.info("test_PageTitle_001 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")

        self.d.get(self.url)
        self.log.info("Go to -->" + self.url)

        if self.d.title == "Your store. Login":
            self.log.info("test_PageTitle_001 is Passed")
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_PageTitle_001_Pass.png")
            assert True
        else:
            self.log.info("test_PageTitle_001 is Failed")
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_PageTitle_001_Fail.png")
            assert False
        self.log.info("test_PageTitle_001 is Completed")


    def test_Login_002(self , setup):
        self.log.info("test_Login_002 is Started")
        self.d = setup
        self.log.info("Launching Browser--!!")
        self.d.get(self.url)
        self.log.info("Go to -->" + self.url)

        self.lp = LoginPage(self.d)
        self.lp.Enter_Email(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Clicked on Login Button")
        if self.lp.Success_MSG() == "Dashboard / nopCommerce administration":
            self.log.info("test_Login_002 is Passed")
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_Login_002_Pass.png")
            self.lp.CLick_Logout()
            self.log.info("Clicked on Logout Button")
            time.sleep(5)
            assert True
        else:
            self.log.info("test_Login_002 is Failed")
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_Login_002_Fail.png")
            assert False
        self.log.info("test_Login_002 is Completed")