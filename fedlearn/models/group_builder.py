from .group import Group
from .builder import Builder

class GroupBuilder(Builder):

    def __init__(self):
        self.name = None
        self.id = None
        self.devices = {}
        self.round_info = {}
        self.round_paths = []
        self.current_round_ids = []
        self.members = {}
        self.billing = {}

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

    def set_round_info(self, round_info):
        """
        :param rounds: dict
        """
        self.round_info = round_info

    def set_round_paths(self, round_paths):
        """
        :param round_paths: list(list(string))
        """
        self.round_paths = round_paths

    def set_current_round_ids(self, current_round_ids):
        """
        :param current_round_ids: list(string)
        """
        self.current_round_ids = current_round_ids

    def set_billing(self, billing):
        """
        :param billing: dict
        """
        self.billing = billing

    def set_members(self, members):
        """
        :param members: dict
        """
        self.members = members

    def build(self):
        self._validate_parameters()

        return Group(self.name,
                     self.id,
                     self.devices,
                     self.round_info,
                     self.round_paths,
                     self.current_round_ids,
                     self.members,
                     self.billing)

    def _validate_parameters(self):
        if self.id is None:
            raise ValueError("ID must not be none")
        elif type(self.id) is not type("str"):
            raise ValueError("ID must be type string")

        if self.name is None:
            raise ValueError("name must not be none")
        elif type(self.name) is not type("str"):
            raise ValueError("name must be type string")
