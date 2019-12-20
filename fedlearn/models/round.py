class Round:

    def __init__(self, id, status):
        """
        :param id: string
        :param status: RoundStatus
        """
        self.id = id
        self.status = status

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status
