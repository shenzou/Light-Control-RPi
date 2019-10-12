from guizero import App, PushButton, Slider
from yeelight import Bulb, discover_bulbs

#discover_bulbs()

light = None
light2 = None

def toggle_light():
    light.toggle()
    if(light2 != None):
        light2.toggle()
    
def set_Alex():
    global light
    light = Bulb("192.168.0.12")
    global light2
    light2 = None
    
def set_Salon():
    global light
    light = Bulb("192.168.0.11")
    global light2
    light2 = Bulb("192.168.0.49")
    
def change_brightness(brightness):
    light.set_brightness(brightness)
#chambreAlex.toggle()
#chambreAlex.toggle()
#chambreAlex.set_brightness(50)
#chambreAlex.set_rgb(255, 0, 0)

app = App(title="Yeelight control")
changeToAlex = PushButton(app, command=set_Alex, text="Switch to Alex")
changeToSalon = PushButton(app, command=set_Salon, text="Switch to Salon")

toggleLight = PushButton(app, command=toggle_light, text="Toggle Light")
brightSlider = Slider(app, command=change_brightness, start=1, end=99)
app.display()

