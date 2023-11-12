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
        username_create = self.ids.username_create_input.text
        email = self.ids.email_input.text
        password_create = self.ids.password_create_input.text
        confirm_password = self.ids.confirm_password_input.text

        if password_create == confirm_password:
            print("Account created successfully!")
            self.manager.current = "LoginPage"
        else:
            print("Account creation failed. Please check your information.")

    def confirm_account(self,username_create, email, password_create):
        confirm_password = "admin"
        confirm_confirm_password = "admin"
        return confirm_password == confirm_confirm_password
    
    def verify_account(self, instance):
        username_create = self.ids.username_create_input.text
        email = self.ids.email_input.text
        password_create = self.ids.password_create_input.text
        confirm_password = self.ids.confirm_password_input.text

        if username_create and email and password_create and confirm_password:
            if password_create == confirm_password:
                # Passwords match, verification successful
                print("Verification successful!")
            else:
                print("Passwords do not match. Please verify.")
        else:
            print("Please fill in all fields.")
    
class LoginPage(AnchorLayout, Screen):
    def login_clicked(self, instance):
        username_login = self.ids.username_input.text
        password_login = self.ids.password_input.text

        if self.check_credentials(username_login, password_login):
            print(f"Login successful! Welcome to PassLock, {username_login}.")
            self.manager.current = "MainPage"
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
class SidebarPage(AnchorLayout,Screen):
    pass
class ToolbarMainAppPage(Screen):
    pass
class MainAppPage(Screen):
    pass
class NavDrawer(MDNavigationDrawer):
    pass
class ForgotPasswordPage(MDAnchorLayout,Screen):
    pass
class ForgotPasswordGridLayoutDesign(AnchorLayout,Screen):
    pass

class PassLockApp(MDApp):
    def navigation_draw(self):
        print('navigation_draw working')

PassLockApp().run()
