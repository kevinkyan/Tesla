STATE_VENT = 'vent'
STATE_CLOSE = 'close'

class Vehicle:
    def __init__(self, api_client, vehicle):
        self._api_client = api_client
        self._vehicle = vehicle
        self._vehicle_id = vehicle['id']

        # self._charge = Charge(self._api_client, vehicle['id'])
        # self._climate = Climate(self._api_client, vehicle['id'])
        # self._commands = Commands(self._api_client, vehicle['id'])

    def get_state(self):
        return self._api_client.get('vehicles/{}/data_request/vehicle_state'.format(self.id))

    def _set_sunroof_state(self, state):
        return self._api_client.post(
            'vehicles/{}/command/sun_roof_control'.format(self._vehicle_id),
            {'state': state}
        )

    def vent_sunroof(self):
        return self._set_sunroof_state(STATE_VENT)

    def close_sunroof(self):
        return self._set_sunroof_state(STATE_CLOSE)

    def flash_lights(self):
        return self._api_client.post('vehicles/{}/command/flash_lights'.format(self._vehicle_id))

    def wake(self):
        return self._api_client.post('vehicles/{}/command/wake_up'.format(self._vehicle_id))

    def honk_horn(self):
        return self._api_client.post('vehicles/{}/command/honk_horn'.format(self._vehicle_id))

    def open_charge_port(self):
        return self._api_client.post('vehicles/{}/command/charge_port_door_open'.format(self._vehicle_id))

    @property
    def id(self):
        return self._vehicle['id']

    @property
    def display_name(self):
        return self._vehicle['display_name']

    @property
    def vin(self):
        return self._vehicle['vin']

    @property
    def state(self):
        return self._vehicle['state']

    @property
    def sun_roof_state(self):
        return self._vehicle['sun_roof_state']
    @property
    def charge(self):
        return self._charge

    @property
    def climate(self):
        return self._climate

    @property
    def controls(self):
        return self._controls

