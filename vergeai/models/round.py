from .round_status import RoundStatus
from .round_configuration import RoundConfiguration

class Round:

    def __init__(self,
                 id,
                 devices,
                 status,
                 configuration,
                 created_on,
                 billable_size,
                 parent_group_id):
        """
        :param id: string
        :param devices: list(string)
        :param status: RoundStatus
        :param configuration: RoundConfiguration
        :param created_on: string
        :param billable_size: string
        :param parent_group_id: string
        """
        self.id = id
        self.devices = devices
        self.status = status
        self.configuration = configuration
        self.created_on = created_on
        self.billable_size = billable_size
        self.parent_group_id = parent_group_id

    def get_id(self):
        return self.id

    def get_devices(self):
        return self.devices

    def get_status(self):
        """
        :return: RoundStatus
        """
        return self.status

    def get_configuration(self):
        """
        :return: RoundConfiguration
        """
        return self.round_configuration

    def get_created_on(self):
        return self.created_on

    def is_complete(self):
        """
        :return: boolean
        """
        return self.get_status() == RoundStatus.COMPLETED

    def is_active(self):
        """
        :return: boolean
        """
        return self.is_in_progress() or self.is_aggregation_in_progress()

    def is_in_initialization(self):
        """
        :return: boolean
        """
        return self.get_status() == RoundStatus.INITIALIZED

    def is_in_progress(self):
        """
        :return: boolean
        """
        return self.get_status() == RoundStatus.IN_PROGRESS

    def is_aggregation_in_progress(self):
        """
        :return: boolean
        """
        return self.get_status() == RoundStatus.AGGREGATION_IN_PROGRESS

    def is_cancelled(self):
        """
        :return: boolean
        """
        return self.get_status() == RoundStatus.CANCELLED

    def contains_device(self, device_id):
        """
        :param device_id: string
        :return: boolean
        """
        return device_id in self.devices

    def get_billable_size(self):
        return int(self.billable_size)

    def get_parent_group_id(self):
        return self.parent_group_id

    def to_json(self):
        return {
            "ID" : self.id,
            "status" : self.status.value,
            "devices" : self.devices,
            "configuration" : self.configuration.to_json(),
            "created_on" : self.created_on,
            "billable_size" : self.billable_size,
            "parent_group_id" : self.parent_group_id
        }

    @staticmethod
    def from_json(json_data):
        return Round(json_data["ID"],
            json_data["devices"],
            RoundStatus(json_data["status"]),
            RoundConfiguration.from_json(json_data["configuration"]),
            json_data["created_on"],
            json_data["billable_size"],
            json_data["parent_group_id"])
