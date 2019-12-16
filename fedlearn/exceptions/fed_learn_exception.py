class FedLearnException(Exception):
    """
    Exception thrown when the API is used incorrectly.
    """

    @property
    def message(self):
        return self.__dict__.get('message', None) or getattr(self, 'args')[0]
