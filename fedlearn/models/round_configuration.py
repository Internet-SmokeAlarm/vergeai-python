class RoundConfiguration:

    def __init__(self, num_devices, device_selection_strategy):
        """
        :param num_devices: string. Number of devices to use in the round
        :param device_selection_strategy: string. Device selection strategy. Can be one of:
            - RANDOM
        """
        self.num_devices = num_devices
        self.device_selection_strategy = device_selection_strategy

    def get_num_devices(self):
        return self.num_devices

    def get_device_selection_strategy(self):
        return self.device_selection_strategy
