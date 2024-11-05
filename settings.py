import os
from dotenv import load_dotenv

class Settings:
    def __init__(self, env_file_path):
        """We initialize the settings file"""
        load_dotenv(env_file_path)

    def get_parameters(self):
        """We read the file containing some constant parameters of the url information"""
        url = os.getenv('URL')
        endpoints = os.getenv('ENDPOINTS').split(',')
        return url, endpoints