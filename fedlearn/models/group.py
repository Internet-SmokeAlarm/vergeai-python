class Group:

    def __init__(self, name, id, devices, rounds, current_round_id, initial_model_set):
        """
        :param name: string. Logical name of this group
        :param id: string. ID of this group
        :param devices: dict
        :param rounds: dict
        :param current_round_id: string
        :param initial_model_set: boolean.
        """
        self.id = id
        self.name = name
        self.devices = devices
        self.rounds = rounds
        self.current_round_id = current_round_id
        self.initial_model_set = initial_model_set

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

    def is_initial_model_set(self):
        """
        :return: boolean
        """
        return self.initial_model_set

    def get_devices(self):
        """
        :return: dict
        """
        return self.devices

    def get_rounds(self):
        """
        :return: dict
        """
        return self.rounds

    def get_current_round_id(self):
        """
        :return: string
        """
        return self.current_round_id
