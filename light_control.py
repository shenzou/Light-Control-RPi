import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider

from yeelight import Bulb, discover_bulbs

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.salon = Button(text="Lumières du salon", font_size=40)
        self.salon.bind(on_press=self.set_Salon)
        self.add_widget(self.salon)

        self.chambreAlex = Button(text="Lumières Alex", font_size=40)
        self.chambreAlex.bind(on_press=self.set_Alex)
        self.add_widget(self.chambreAlex)

        self.toggle = Button(text="Allumer/Eteindre", font_size=40)
        self.toggle.bind(on_press=self.toggle_light)
        self.add_widget(self.toggle)

        self.toggleState = Label(text="Résultat: ", markup = True)
        self.add_widget(self.toggleState)

        self.brightSlider = Slider(min=0, max=100, value=50)
        self.brightSlider.bind(on_value=self.change_brightness)
        self.add_widget(self.brightSlider)

        # self.add_widget(Label(text="Email: "))
        # self.email = TextInput(multiline=False)
        # self.add_widget(self.email)
    
    def pressed(self, instance):
        None
        # name = self.name.text
        # last = self.lastName.text
        # email = self.email.text

        # print("Name:", name, "Last Name:", last, "Email:", email)
        # self.name.text = ""
        # self.lastName.text = ""
        # self.email.text = ""

    light = None
    light2 = None

    def toggle_light(self, instance):
        try:
            if(light != None):
                light.toggle()
            if(light2 != None):
                light2.toggle()
            print("Changed light state.")
            self.toggleState.text = "Résultat: [color=00FF00]OK ![/color]"
        except:
            self.toggleState.text = 'Résultat: [color=ff0000]Echec ![/color]'
            pass
        
        
    def set_Alex(self, instance):
        global light
        light = Bulb("192.168.0.12")
        global light2
        light2 = None
        print("Changed to Alex")
        
    def set_Salon(self, instance):
        global light
        light = Bulb("192.168.0.11")
        global light2
        light2 = Bulb("192.168.0.49")
        print("Changed to Salon")
        
    def change_brightness(self, instance):
        # try:
        #     print("Changing brightness: ", brightness)
        #     if(light != None):
        #         light.set_brightness(int(brightness))
        #     if(light2 != None):
        #         light2.set_brightness(int(brightness))
        # except:
        #     pass
        print(self)
        

class MyApp(App):
    def build(self):
       return MyGrid()


if __name__ == "__main__":
    MyApp().run()