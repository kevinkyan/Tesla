from tesla_api import TeslaApp

client = TeslaApp('user', 'pass')

vehicles = client.get_vehicles()

for v in vehicles:
    print(v.vin)
    v.wake()
    v.flash_lights()
