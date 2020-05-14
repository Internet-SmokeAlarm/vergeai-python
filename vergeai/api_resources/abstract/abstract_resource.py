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
