from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
import os
os.chdir('E:\\Python\\Python Courses\\Kivy')

class Demo(GridLayout):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    
    def on_click(self):
        print("Your Name Is {} And You Are {} Years Old".format(self.name.text,self.age.text))
        
        self.name.text =""
        self.age.text = ""
        
class MyFirstApp(App):
    def build(self):
        return Demo()

MyFirstApp().run()

