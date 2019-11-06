from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window

Window.clearcolor=.3,.3,.3,1


class Calculate(Screen):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except:
                self.display.text="Error"

class Properties(Screen):
    pass

class Setting(Screen):
    pass

class Window(ScreenManager):
    pass

class Calc(App):
    def build(self):
        return Window()

if __name__=="__main__":
    Calc().run()
