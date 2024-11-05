import requests

class MyRequests:
    def __init__(self, url, endpoints):
        """We initialize the class with the url information for the requests"""
        self.url = url
        self.endpoints = endpoints
        self.web_data = {}

    def get_requests(self):
        """We try to get the requests and then we return them"""
        for endpoint in self.endpoints:
            full_url = self.url + endpoint
            response = requests.get(full_url)
            if response.status_code == 200:
                MyRequests._get_endpoint_data(self, response, full_url, endpoint)
            else:
                print(f'The request to {full_url} has failed with the status code {response.status_code}')
        return self.web_data

    def _get_endpoint_data(self, response, full_url, endpoint):
        """We try to get the data from an endpoint"""
        try:
            endpoint_data = response.json()
        except ValueError:
            print(f'The response to {full_url} doesn\'t have JSON format')
        else:
            endpoint_key = endpoint.replace('/', '').capitalize()
            self.web_data[endpoint_key] = endpoint_data

