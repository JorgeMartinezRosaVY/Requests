from requests_manager import RequestsManager

if __name__ == '__main__':
    """We create an instance of RequestsManager to run the whole program"""
    env_file_path = 'input_files/config.env'
    requests_manager = RequestsManager(env_file_path)
    requests_manager.run()