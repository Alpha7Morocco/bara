from kivy.app import App  #istid3a a  tatbik
from kivy.lang import Builder # intid3a a milaf kharigiy
from kivy.core.window import Window #tahakom fi size + color
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor=(100/255.0,0,1,1) # "red, green, blue,a" hada kod litandif nafida mina al alwan 0=>255
Window.size=(1,1)  # "width, height" tahakom fi hagm nafida

class Error(Screen):
    pass
class Maintree(ScreenManager):
    pass
class Mainone(Screen):
    pass
class Maintow(Screen):
    pass
kv= """
Maintree:
    Mainone:
    Maintow:
    Error:
<Mainone>:
    name:"home"
    GridLayout:
        cols:1
        GridLayout:
            padding:10
            rows:4
            #istid3a sora
            #Image:
             #   source:""
            AnchorLayout:
                AsyncImage:
                    size_hint:None,None
                    size:dp(80),dp(80)
                    source:"https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-white-512.png"

            Label:
                text:'Learn Python'
                font_size: 22 # hagm kitaba
            Label:
                text:'please enter pwd'
                size_hint:0.1,0.3 
            TextInput:
                id:pwd # litakhsis 
                text:"enter your pwd" 
                password:True # li ikhfa a al kod
                multiline: False #liman3 nozol ila satr tani
                size_hint:.1,.2
        Button:
            text:"login"  
            size_hint:.1,.1 
            on_release:
                
                app.root.current="page1" if pwd.text=="mama" else "Error"   
                root.manager.transition.direction="down"
<Maintow>:
    name:"page1"
    GridLayout:
        cols:1
        GridLayout:
            rows:2
            Image:
                source:"1.jpeg"
            Label
                text:"welcome to my home"
        GridLayout:
            cols:2
            rows:3
            Button:
                text:"php"
                size_hint:.1,.1
            Button:
                text:"python"
                size_hint:.1,.1
            Button:
                text:"html"
                size_hint:.1,.1
            Button:
                text:"java"
                size_hint:.1,.1
            Button:
                text:"nan"
                size_hint:.1,.1
            Button:
                text:"css"
                size_hint:.1,.1
        Button:
            text:"Go Back"
            size_hint:.1,.3
            on_release:
                app.root.current="home"
                root.manager.transition.direction="left"

<Error>:
    name:"Error"
    GridLayout:
        cols:1
        rows:3
        Image:
            source:"1.jpeg"
        Label:
            text:"password Encorrect"
        Button:
            text:"try again"
            size_hint:.1,.1
            on_release:
                app.root.current="home"
                root.manager.transition.direction="right"

"""
nano = Builder.load_string(kv)

class My_app(App):
    def build(self):
        self.title="mama" # ta4yira 3onwan app
        return nano
    



if __name__ =="__main__":
    My_app().run()


