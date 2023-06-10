import configparser

config = configparser.RawConfigParser()
config.read("D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common data' , 'url')
        return url

    @staticmethod
    def getUsername():
        Username = config.get('common data', 'username')
        return Username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password