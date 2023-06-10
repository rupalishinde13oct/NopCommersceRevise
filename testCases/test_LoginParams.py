import time

from PageObjects.LoginPage import LoginPage
from Utility.Logger import Logging
from Utility.readConfig import ReadConfig


class TestLoginParam:
    url = ReadConfig.getURL()
    log = Logging.logGen()

    def test_LoginParams_003(self , setup , getLoginData):

        self.log.info("test_LoginParams_003 is Started")
        self.d = setup
        self.log.info("Launching Browser--!!")
        self.d.get(self.url)
        self.log.info("Go to -->" + self.url)

        self.lp = LoginPage(self.d)

        self.lp.Enter_Email(getLoginData[0])
        self.log.info("Entering Username-->" + getLoginData[0])
        self.lp.Enter_Password(getLoginData[1])
        self.log.info("Entering Password-->" + getLoginData[1])
        self.lp.Click_Login()
        self.log.info("Clicked on Login Button")

        status = []
        if self.lp.Success_MSG() == "Dashboard / nopCommerce administration":
            if getLoginData[2] == "Pass":
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_LoginParams_003_Pass.png")
                self.lp.CLick_Logout()
                self.log.info("Clicked on Logout Button")
                # time.sleep(5)
                status.append("Pass")

            else:
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_LoginParams_003_Fail.png")
                # time.sleep(5)
                status.append("Fail")
        else:
            if getLoginData[2] == "Fail":
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_LoginParams_003_Pass.png")
                status.append("Pass")

            else:
                self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_LoginParams_003_Fail.png")
                status.append("Fail")

        if "Pass" in status:
            self.log.info("test_LoginParams_003 is Passed")
            assert True
        else:
            self.log.info("test_LoginParams_003 is Failed")
            assert False

        self.log.info("test_LoginParams_003 is Completed")