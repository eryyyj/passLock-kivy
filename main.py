from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.recycleview import RecycleView

class LoginPage(AnchorLayout):
    pass
class CreateAccountPage(AnchorLayout):
    pass
class SidebarPage(AnchorLayout):
    pass
class passList(RecycleView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.data = [{'text':str(i)} for i in range(20)]
class PasslockPage(MDAnchorLayout):
    pass
class MainAppPage(PageLayout):
    pass
class PassLockApp(MDApp):
    pass

PassLockApp().run()