import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider

from yeelight import Bulb, discover_bulbs

import vars

       

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

        global toggleState
        toggleState = Label(text="Résultat: ", markup = True)
        self.add_widget(toggleState)


        self.add_widget(LumGrid())
        self.add_widget(RGBGrid())

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
            toggleState.text = "Résultat: [color=00FF00]OK ![/color]"
        except:
            toggleState.text = 'Résultat: [color=ff0000]Echec ![/color]'
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
        
    

class LumGrid(GridLayout):
    def __init__(self):
        GridLayout.__init__(self, cols=1, rows=2)

        self.brightLabel = Label(text="Luminosité")
        self.add_widget(self.brightLabel)
        self.brightSlider = Slider(min=0, max=100, value=50)
        self.brightSlider.fbind('value', self.change_brightness)
        self.add_widget(self.brightSlider)

    def change_brightness(self, instance, val):
        try:
            print("Changing brightness: ", int(val))
            if(light != None):
                light.set_brightness(int(val))
            if(light2 != None):
                light2.set_brightness(int(val))
            toggleState.text = "Résultat: [color=00FF00]OK ![/color]"
        except:
            toggleState.text = 'Résultat: [color=ff0000]Echec ![/color]'
            pass


class RGBGrid(GridLayout):

    def __init__(self):
        GridLayout.__init__(self, cols=1, rows=6)

        if(vars.red == None): 
            vars.red = 255
        if(vars.green == None): 
            vars.green = 255
        if(vars.blue == None): 
            vars.blue = 255

        self.redSlider = Slider(min=0, max=255, value=vars.red)
        self.redSlider.fbind('value', self.change_red)
        self.greenSlider = Slider(min=0, max=255, value=vars.green)
        self.greenSlider.fbind('value', self.change_green)
        self.blueSlider = Slider(min=0, max=255, value=vars.blue)
        self.blueSlider.fbind('value', self.change_blue)

        self.redText = Label(text="Rouge", markup = True)
        self.add_widget(self.redText)
        self.add_widget(self.redSlider)

        self.greenText = Label(text="Vert", markup = True)
        self.add_widget(self.greenText)
        self.add_widget(self.greenSlider)

        self.blueText = Label(text="Bleu", markup = True)
        self.add_widget(self.blueText)
        self.add_widget(self.blueSlider)

        

    def change_blue(self, instance, val):
        try:
            vars.blue = val
            if(light != None):
                light.set_rgb(int(vars.red), int(vars.green), int(vars.blue))
            if(light2 != None):
                light2.set_rgb(int(vars.red), int(vars.green), int(vars.blue))
            toggleState.text = "Résultat: [color=00FF00]OK ![/color]"
            print(vars.red, vars.green, vars.blue)
        except:
            toggleState.text = 'Résultat: [color=ff0000]Echec ![/color]'
            pass
        

    def change_green(self, instance, val):
        try:
            vars.green = val
            if(light != None):
                light.set_rgb(int(vars.red), int(vars.green), int(vars.blue))
            if(light2 != None):
                light2.set_rgb(int(vars.red), int(vars.green), int(vars.blue))
            toggleState.text = "Résultat: [color=00FF00]OK ![/color]"
            print(vars.red, vars.green, vars.blue)
        except:
            toggleState.text = 'Résultat: [color=ff0000]Echec ![/color]'
            pass


    def change_red(self, instance, val):
        try:
            vars.red = val
            if(light != None):
                light.set_rgb(int(vars.red), int(vars.green), int(vars.blue))
            if(light2 != None):
                light2.set_rgb(int(vars.red), int(vars.green), int(vars.blue))
            toggleState.text = "Résultat: [color=00FF00]OK ![/color]"
            print(vars.red, vars.green, vars.blue)
        except:
            toggleState.text = 'Résultat: [color=ff0000]Echec ![/color]'
            pass

class MyApp(App):
    def build(self):
       return MyGrid()


if __name__ == "__main__":
    MyApp().run()