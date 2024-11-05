from my_requests import MyRequests
from settings import Settings

class RequestsManager:
    def __init__(self,env_file_path):
        """We initialize the class by calling Settings to obtain some constant parameters"""
        self.config = Settings(env_file_path)
        self.url, self.endpoints = self.config.get_parameters()

    def run(self):
        """We call the rest of the methods"""
        web_data = self._get_web_data()
        self._print_web_data(web_data)

    def _get_web_data(self):
        """We create an instance of MyRequests to obtain and return the url requests"""
        mock_requests = MyRequests(self.url, self.endpoints)
        web_data = mock_requests.get_requests()
        return web_data

    def _print_web_data(self, web_data):
        """We print the url along with the requests obtained and their keys"""
        print(f'These are some of the data from {self.url}:')
        for key, value in web_data.items():
            print(f'\n{key}: \n{value[:5]}')
