from .. import APIRequestor

class AbstractAPIResource:

    OBJECT_NAME = None

    @classmethod
    def class_url(cls):
        """
        Returns the relative URL for this resource.

        :return: string
        """
        if cls == AbstractAPIResource:
            raise NotImplementedError("get_resource_url() not implemented")

        return cls.OBJECT_NAME

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
