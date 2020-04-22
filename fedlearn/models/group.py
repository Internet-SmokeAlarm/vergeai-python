class Group:

    def __init__(self,
                 name,
                 id,
                 devices,
                 round_info,
                 round_paths,
                 current_round_ids,
                 members,
                 billing):
        """
        :param name: string. Logical name of this group
        :param id: string. ID of this group
        :param devices: dict
        :param round_info: dict. Contains overview information about registered rounds
        :param round_paths: list(list(string)). Details the progression of rounds
        :param current_round_ids: list(string). Rounds that are active in this group
        :param members: dict. Information about the members in this group.
        :param billing: dict. Billing information pertaining to this group.
        """
        self.id = id
        self.name = name
        self.devices = devices
        self.round_info = round_info
        self.round_paths = round_paths
        self.current_round_ids = current_round_ids
        self.members = members
        self.billing = billing

    def get_name(self):
        """
        :return: string
        """
        return self.name

    def get_id(self):
        """
        :return: string
        """
        return self.id

    def get_devices(self):
        """
        :return: dict
        """
        return self.devices

    def get_round_info(self):
        """
        :return: dict
        """
        return self.round_info

    def get_round_paths(self):
        return self.round_paths

    def get_current_round_ids(self):
        """
        :return: list(string)
        """
        return self.current_round_ids

    def get_members(self):
        """
        :return: dict
        """
        return self.members

    def get_billing(self):
        """
        :return: dict
        """
        return self.billing

    def to_json(self):
        return {
            "name" : self.name,
            "ID" : self.id,
            "devices" : self.devices,
            "round_info" : self.round_info,
            "round_paths" : self.round_paths,
            "current_round_ids" : self.current_round_ids,
            "members" : self.members,
            "billing" : self.billing
        }

    @staticmethod
    def from_json(json_data):
        return Group(json_data["name"],
                     json_data["ID"],
                     json_data["devices"],
                     json_data["round_info"],
                     json_data["round_paths"],
                     json_data["current_round_ids"],
                     json_data["members"],
                     json_data["billing"])
