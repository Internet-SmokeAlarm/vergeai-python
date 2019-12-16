class FedLearnApiException(Exception):
    """
    Exception thrown when the API responds with an error.
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]
