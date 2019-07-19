from tesla_api import TeslaApp

client = TeslaApp('kevyan1998@gmail.com', 'Sushi1029')

vehicles = client.get_vehicles()

for v in vehicles:
    print(v.vin)
    v.wake()
    v._set_sunroof_state('vent')
    v.flash_lights()
    v._set_sunroof_state('close')
