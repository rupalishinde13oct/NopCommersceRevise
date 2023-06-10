import time
from Utility.readXLLoginData import XLUtil
from PageObjects.LoginPage import LoginPage
from Utility.readConfig import ReadConfig
from Utility.Logger import Logging
class TestLoginDDT:

    url = ReadConfig.getURL()
    log = Logging.logGen()
    path = "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\TestData\\LoginData.xlsx"

    def test_LoginDDT_004(self, setup):
        self.log.info("test_LoginDDT_004 is Started")
        self.d = setup
        self.log.info("Launching Browser--!!")
        self.d.get(self.url)
        self.log.info("Go to -->" + self.url)

        self.lp = LoginPage(self.d)
        status = []
        self.row = XLUtil.getRowCount(self.path , "Sheet1")
        for i in range(2 , self.row+1):

            self.username = XLUtil.readXLData(self.path , "Sheet1" , i , 2)
            self.password = XLUtil.readXLData(self.path, "Sheet1", i, 3)

            self.lp.Enter_Email(self.username)
            self.log.info("Entering Username-->" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering Password-->" + self.password)
            self.lp.Click_Login()
            self.log.info("Clicked on Login Button")

            if self.lp.Success_MSG() == "Dashboard / nopCommerce administration":
                if XLUtil.readXLData(self.path, "Sheet1", i, 4) == "Pass":
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_LoginDDT_004_Pass.png")
                    XLUtil.writeXLData(self.path, "Sheet1", i, 5, "Pass")
                    self.lp.CLick_Logout()
                    self.log.info("Clicked on Logout Button")
                    status.append("Pass")


                else:
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_LoginDDT_004_Fail.png")
                    self.lp.CLick_Logout()
                    XLUtil.writeXLData(self.path, "Sheet1", i, 5, "Fail")
                    self.log.info("Clicked on Logout Button")
                    status.append("Fail")

            else:
                if XLUtil.readXLData(self.path, "Sheet1", i, 4) == "Fail":
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_LoginDDT_004_Pass.png")
                    status.append("Pass")
                    XLUtil.writeXLData(self.path, "Sheet1", i, 5, "Pass")
                else:
                    self.d.save_screenshot(
                    "D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Screenshots\\test_LoginDDT_004_Fail.png")
                    status.append("Fail")
                    XLUtil.writeXLData(self.path, "Sheet1", i, 5, "Fail")

            if "Pass" in status:
                self.log.info("test_LoginDDT_004 is Passed")
                assert True
            else:
                self.log.info("test_LoginDDT_004 is Failed")
                assert False
            self.log.info("test_LoginDDT_004 is Completed")