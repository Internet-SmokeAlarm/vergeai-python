class Device:

    def __init__(self, id, api_key):
        self.id = id
        self.api_key = api_key

    def get_id(self):
        return self.id

    def get_api_key(self):
        return self.api_key
