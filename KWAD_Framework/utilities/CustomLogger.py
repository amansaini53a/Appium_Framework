import inspect
import logging
import allure

def customLogger():
    # Used to get the class/method name from where the custom logger is called
    logName = inspect.stack()[1][3]
    #Create the logging object and pass the logName in it
    logger = logging.getLogger(logName)
    #Set the log level
    logger.setLevel(logging.DEBUG)
    #Create the fileHandler to save the logs in the File
    fileHandler = logging.FileHandler("../reports/test.log",mode='w')
    #Set the log level for fileHandler
    fileHandler.setLevel(logging.DEBUG)
    #Create the formatter in which format we want to save the logs
    formatter = logging.Formatter("%(asctime)s : %(name)s : %(levelname)s %(message)s",datefmt= "%d/%m/%y  %I:%M:%S  %p  %A")
    #Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)
    #Add fileHandler to Logging
    logger.addHandler(fileHandler)
    return logger


def allureLogs(text):
    with allure.step(text):
        pass