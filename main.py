from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout


class LoginPage(AnchorLayout):
    pass
class CreateAccountPage(AnchorLayout):
    pass
class SidebarPage(AnchorLayout):
    pass
class MainAppPage(MDAnchorLayout):
    pass
class PassLockApp(MDApp):
    pass

PassLockApp().run()