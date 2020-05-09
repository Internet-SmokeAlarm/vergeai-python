from .. import APIRequestor

class AbstractType:

    @staticmethod
    def _simple_request(cls, action, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param action: string
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        requestor = APIRequestor(
            api_key=api_key,
            api_version=api_version,
            gateway=gateway)
        url = cls.class_url()

        return requestor.request("post", url, action, parameters)
