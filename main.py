from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.theming import ThemeManager
from kivy.uix.scrollview import ScrollView

Window.size = (300,500)

class PageManager(ScreenManager):
    pass
class CreateAccountPage(AnchorLayout, Screen):
    def create_account(self, instance):
        username = self.ids.username_input.text
        email = self.ids.email_input.text
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text

        if self.verify_account(username, email, password, confirm_password):
            # Add create the account in the database
            print("Account created successfully!")
            self.manager.current = "LoginPage"
        else:
            print("Account creation failed. Please check your information.")

    def verify_account(self, username, email, password, confirm_password):
        valid_password = "admin"
        valid_confirm_password = "admin"
        return valid_password == valid_confirm_password
    
class LoginPage(AnchorLayout, Screen):
    def login_clicked(self, instance):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        if self.check_credentials(username, password):
            print(f"Login successful! Welcome to PassLock, {username}.")
        else:
            print("Login failed. Invalid username or password.")

    def check_credentials(self, username, password):
        check_username = "admin"
        check_password = "admin"

        return username == check_username and password == check_password

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

class PassLockApp(MDApp):
    def navigation_draw(self):
        print('navigation_draw working')

PassLockApp().run()
