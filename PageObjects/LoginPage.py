from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:

    XPATH_Email = (By.XPATH , "//input[@id='Email']")
    XPATH_Password = (By.CSS_SELECTOR , "input[id='Password']")
    XPATH_Login = (By.XPATH , "//button[@type='submit']")
    XPATH_Success_MSG = "Dashboard / nopCommerce administration"
    XPATH_Logout = (By.XPATH , "//a[normalize-space()='Logout']")

    def __init__(self , d):
        self.d = d

    def Enter_Email(self , email):
        self.d.find_element(*LoginPage.XPATH_Email).clear()
        self.d.find_element(*LoginPage.XPATH_Email).send_keys(email)

    def Enter_Password(self , password):
        self.d.find_element(*LoginPage.XPATH_Password).clear()
        self.d.find_element(*LoginPage.XPATH_Password).send_keys(password)

    def Click_Login(self):
        self.d.find_element(*LoginPage.XPATH_Login).click()

    def CLick_Logout(self):
        self.d.find_element(*LoginPage.XPATH_Logout).click()

    def Success_MSG(self):
        try:
            self.d.find_element(*LoginPage.XPATH_Logout)
            # return True
            titile = self.d.title
        except NoSuchElementException:
            # return False
            titile = self.d.title
        return titile