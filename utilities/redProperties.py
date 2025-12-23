import configparser
import os

config = configparser.RawConfigParser()

config_path = os.path.join(
    os.path.dirname(__file__),   # <-- THIS IS THE FIX
    "..",
    "Configurations",
    "config.ini"
)

config.read(config_path)

# DEBUG (keep for now)
print("CONFIG FILE PATH:", config_path)
print("CONFIG SECTIONS:", config.sections())

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get('commonInfo', 'baseURL')

    @staticmethod
    def getValidEmail():
        return config.get('login', 'valid_email')

    @staticmethod
    def getValidPassword():
        return config.get('login', 'valid_password')

    @staticmethod
    def getInvalidEmail():
        return config.get('invalidLogin', 'invalid_email')

    @staticmethod
    def getInvalidPassword():
        return config.get('invalidLogin', 'invalid_password')



