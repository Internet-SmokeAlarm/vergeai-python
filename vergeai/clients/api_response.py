class APIResponse:

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __str__(self):
        return "[APIResponse (status_code: {}), (data: {})]".format(self.status_code, self.data)
