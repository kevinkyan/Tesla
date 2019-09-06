from kivy.app import App
from kivy.app import Widget
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from tesla_api import TeslaApp
import os
//schedule for MWF 9:40 & 2:20
//schedule for T 11:40
//schedule for Th 1:15

client = TeslaApp(os.environ['EMAIL'], os.environ['PASSWORD'])
print(os.environ['EMAIL'], os.environ['PASSWORD'])

if 'EMAIL' not in os.environ:
    raise Exception('DID NOT FIND EMAIL IN ENV')
if 'PASSWORD' not in os.environ:
    raise Exception('DID NOT FIND PASSWORD IN ENV')


vehicles = client.list_vehicles()
v = vehicles[0]
print("VIN:{}".format(v.vin))
def prep_car(instance):
    v.wake()
    //heat up car
def sunroof(instance):
        v.wake()
        v._set_sunroof_state('vent')
        v.flash_lights()
        v._set_sunroof_state('close')
        print('complete')
def honk(instance):
    v.wake()
    v.honk_horn()
    print('complete')

class TeslaWidget(Widget):
    pass
class MyTeslaApp(App):
    def build(self):
        parent = Widget()
        print("what now?")
        btn = Button(text ="sunroof")
        btn.bind(on_press = sunroof)
        parent.add_widget(btn)
        return parent
if __name__ == '__main__':
    MyTeslaApp().run()
