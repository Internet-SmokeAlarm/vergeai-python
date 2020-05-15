from abc import abstractmethod

class AbstractClient:

    @abstractmethod
    def post(self, headers, url, data={}):
        raise NotImplementedError("post() not implemented")

    @abstractmethod
    def get(self, headers, url):
        raise NotImplementedError("get() not implemented")
