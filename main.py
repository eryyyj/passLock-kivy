from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.theming import ThemeManager
from kivy.uix.scrollview import ScrollView
Window.size = (300,500)
class CreateAccountPage(AnchorLayout):
    pass
class LoginPage(AnchorLayout):
    pass
class passList(RecycleView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.data = [{'text':str(i)} for i in range(20)]
class PasslistPage(MDAnchorLayout):
    pass
class SidebarPage(AnchorLayout):
    pass
class ToolbarMainAppPage(Screen):
    pass
class MainAppPage(Screen):
    pass
class NavDrawer(MDNavigationDrawer):
    pass
class ForgotPasswordPage(MDAnchorLayout):
    pass
class ForgotPasswordGridLayoutDesign(AnchorLayout):
    pass
class CreateAccountSuccessfulPage(AnchorLayout):
    pass
class AddCredentialsPage(AnchorLayout):
    pass
class CredentialsCreatedPage(MDAnchorLayout):
    pass
class PassLockApp(MDApp):
    def navigation_draw(self):
        print('navigation_draw working')

PassLockApp().run()