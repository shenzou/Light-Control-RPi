from guizero import App, PushButton, Slider
from yeelight import Bulb, discover_bulbs

#print(discover_bulbs())

light = None
light2 = None

def toggle_light():
    if(light != None):
        light.toggle()
    if(light2 != None):
        light2.toggle()
    print("Changed light state.")
    
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
    print("Changing brightness: ", brightness)
    if(light != None):
        light.set_brightness(int(brightness))
    if(light2 != None):
        light2.set_brightness(int(brightness))
#chambreAlex.toggle()
#chambreAlex.toggle()
#chambreAlex.set_brightness(50)
#chambreAlex.set_rgb(255, 0, 0)

app = App(title="Yeelight control")

#Creating widgets and binding actions to it.
changeToAlex = PushButton(app, command=set_Alex, text="Switch to Alex")
changeToSalon = PushButton(app, command=set_Salon, text="Switch to Salon")
toggleLight = PushButton(app, command=toggle_light, text="Toggle Light")
brightSlider = Slider(app, command=change_brightness, start=0, end=100)

app.display()

