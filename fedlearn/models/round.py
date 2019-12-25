from .round_status import RoundStatus

class Round:

    def __init__(self, id, status, previous_round_id):
        """
        :param id: string
        :param status: RoundStatus
        :param previous_round_id: string
        """
        self.id = id
        self.status = status
        self.previous_round_id = previous_round_id

    def get_id(self):
        return self.id

    def get_status(self):
        return self.status

    def get_previous_round_id(self):
        return self.previous_round_id

    def is_completed(self):
        return self.status == RoundStatus.COMPLETED
