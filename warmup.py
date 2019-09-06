from tesla_api import TeslaApp
from util import c_to_f
import os


COMFORTABLE_TEMPERATURE = 75

client = TeslaApp(os.environ['EMAIL'], os.environ['PASSWORD'])

vehicles = client.list_vehicles()
v = vehicles[0]
v.wake()
v.climate.set_temperature(23)
v.climate.start_climate()
while(True):
    temp = int(c_to_f.c_to_f(v.climate.get_state()['inside_temp']))
    if temp > COMFORTABLE_TEMPERATURE:
        #send me a notif
        break
