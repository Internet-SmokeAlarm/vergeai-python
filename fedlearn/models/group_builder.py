from .group import Group
from .builder import Builder

class GroupBuilder(Builder):

    def __init__(self):
        self.name = None
        self.id = None
        self.devices = {}
        self.rounds = {}
        self.current_round_id = "N/A"
        self.is_initial_model_set = False

    def set_name(self, name):
        """
        :param name: string
        """
        self.name = name

    def set_id(self, id):
        """
        :param id: string
        """
        self.id = id

    def set_devices(self, devices):
        """
        :param devices: dict
        """
        self.devices = devices

    def set_rounds(self, rounds):
        """
        :param rounds: dict
        """
        self.rounds = rounds

    def set_current_round_id(self, current_round_id):
        """
        :param current_round_id: string
        """
        self.current_round_id = current_round_id

    def set_is_initial_model_set(self, is_initial_model_set):
        """
        :param is_initial_model_set: boolean
        """
        self.is_initial_model_set = is_initial_model_set

    def build(self):
        self._validate_paramaters()

        return Group(self.name, self.id, self.devices, self.rounds, self.current_round_id, self.is_initial_model_set)

    def _validate_paramaters(self):
        if self.id is None:
            raise ValueError("ID must not be none")
        elif type(self.id) is not type("str"):
            raise ValueError("ID must be type string")

        if self.name is None:
            raise ValueError("name must not be none")
        elif type(self.name) is not type("str"):
            raise ValueError("name must be type string")
