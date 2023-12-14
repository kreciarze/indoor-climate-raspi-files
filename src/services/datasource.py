import json


class Datasource:
    def __init__(
            self,
            bt_token="krecik_krol",
            conf_file='conf/datasource.json'
    ):
        self._BT_TOKEN = bt_token
        self.conf_file = conf_file

        data = self.load_data_from_file()

        self.wifi_ssid = data['wifi_ssid']
        self.wifi_password = data['wifi_password']

        self.host = data['host']
        self.port = data['port']
        self.user = data['user']
        self.auth_token = data['auth_token']

    def load_data_from_json(self, data, save=True):

        if 'bt_token' not in data:
            raise RuntimeError("D: Invalid data")

        if self._BT_TOKEN != data['bt_token']:
            raise RuntimeError("T: Invalid bt_token")

        if 'wifi_ssid' not in data \
                or 'wifi_password' not in data \
                or 'host' not in data \
                or 'port' not in data \
                or 'user' not in data \
                or 'auth_token' not in data:
            raise RuntimeError("D: Invalid data")

        self.wifi_ssid = data['wifi_ssid']
        self.wifi_password = data['wifi_password']

        self.host = data['host']
        self.port = data['port']
        self.user = data['user']
        self.auth_token = data['auth_token']

        if save:
            self.save_data_to_file()

    def load_data_from_file(self):
        with open(self.conf_file, 'r') as f:
            return json.load(f)

    def save_data_to_file(self):
        with open(self.conf_file, 'w') as f:
            data = {
                'wifi_ssid': self.wifi_ssid,
                'wifi_password': self.wifi_password,
                'host': self.host,
                'port': self.port,
                'user': self.user,
                'auth_token': self.auth_token
            }
            json.dump(data, f, indent=4)
            f.write('\n')

    def reset_data(self):
        self.wifi_ssid = None
        self.wifi_password = None
        self.host = None
        self.port = None
        self.user = None
        self.auth_token = None
        self.save_data_to_file()

    def is_configured(self):
        return self.wifi_ssid is not None \
            and self.wifi_password is not None \
            and self.host is not None \
            and self.port is not None \
            and self.user is not None \
            and self.auth_token is not None

    def get_bt_token(self):
        return self._BT_TOKEN

    def set_bt_token(self, bt_token):
        self._BT_TOKEN = bt_token
        self.save_data_to_file()

    def get_wifi_ssid(self):
        return self.wifi_ssid

    def set_wifi_ssid(self, wifi_ssid):
        self.wifi_ssid = wifi_ssid
        self.save_data_to_file()

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host
        self.save_data_to_file()

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port
        self.save_data_to_file()

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user
        self.save_data_to_file()

    def get_auth_token(self):
        return self.auth_token

    def set_auth_token(self, auth_token):
        self.auth_token = auth_token
        self.save_data_to_file()

    def __stringify_none(self, value):
        if value is None:
            return "None"
        else:
            return value

    def __str__(self):
        return "wifi_ssid: " + self.__stringify_none(self.wifi_ssid) + "\n" + \
            "wifi_password: " + self.__stringify_none(self.wifi_password) + "\n" + \
            "host: " + self.__stringify_none(self.host) + "\n" + \
            "port: " + self.__stringify_none(self.port) + "\n" + \
            "user: " + self.__stringify_none(self.user) + "\n" + \
            "auth_token: " + self.__stringify_none(self.auth_token)
