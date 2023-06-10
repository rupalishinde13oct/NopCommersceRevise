import logging


class Logging:

    @staticmethod
    def logGen():

        logger = logging.getLogger()

        file = logging.FileHandler("D:\\Rupali Prathamesh Pandit\\NopCommerseRevise\\Logs\\NopCommersLogFile.log")
        format = logging.Formatter(" %(asctime)s : %(lineno)s : %(levelno)s : %(funcName)s : %(message)s :")
        file.setFormatter(format)

        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
