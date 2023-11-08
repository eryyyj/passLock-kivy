from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginPage(AnchorLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        
        username_input = TextInput(hint_text="Enter username here")
        password_input = TextInput(hint_text="Enter password here", password=True)
        login_button = Button(text="Login")
        forgot_password_button = Button(text="Forgot Password")
        create_account_button = Button(text="Create Account")

        
        login_button.bind(on_release=self.on_login_button_click)
        forgot_password_button.bind(on_release=self.on_forgot_password_button_click)
        create_account_button.bind(on_release=self.on_create_account_button_click)

        
        self.add_widget(username_input)
        self.add_widget(password_input)
        self.add_widget(login_button)
        self.add_widget(forgot_password_button)
        self.add_widget(create_account_button)

    def on_login_button_click(self, instance):
        username = self.children[0].text
        password = self.children[1].text
        
        if username == "your_username" and password == "your_password":
            print("Login successful")
            
        else:
            print("Login failed")
            
    def on_forgot_password_button_click(self, instance):
        print("Forgot Password clicked")
        
    def on_create_account_button_click(self, instance):
        print("Create Account clicked")
        
class CreateAccountPage(AnchorLayout):
    def __init__(self, app, **kwargs):
        super(CreateAccountPage, self).__init__(**kwargs)
        self.app = app

    
        username_input = TextInput(hint_text="Enter username")
        email_input = TextInput(hint_text="Enter email")
        password_input = TextInput(hint_text="Enter password", password=True)
        confirm_password_input = TextInput(hint_text="Confirm password", password=True)
        create_account_button = Button(text="Create Account")
        back_to_login_button = Button(text="Back To Login")

        
        create_account_button.bind(on_release=self.on_create_account_button_click)
        back_to_login_button.bind(on_release=self.on_back_to_login_button_click)

       
        self.add_widget(username_input)
        self.add_widget(email_input)
        self.add_widget(password_input)
        self.add_widget(confirm_password_input)
        self.add_widget(create_account_button)
        self.add_widget(back_to_login_button)

    def on_create_account_button_click(self, instance):
        username = self.children[0].text
        email = self.children[1].text
        password = self.children[2].text
        confirm_password = self.children[3].text

        if password == confirm_password:
            print(f"Account created for username: {username} with email: {email}")
            self.app.switch_to_login()
        else:
            print("Password confirmation does not match.")

    def on_back_to_login_button_click(self, instance):
        self.app.switch_to_login()
        
class SidebarPage(BoxLayout):
    def __init__(self, app, **kwargs):
        super(SidebarPage, self).__init__(**kwargs)
        self.app = app

        all_items_button = Button(text="All Items")
        logins_button = Button(text="Logins")
        personal_button = Button(text="Personal")
        history_button = Button(text="History")
        trash_button = Button(text="Trash")

        all_items_button.bind(on_release=self.on_all_items_button_click)
        logins_button.bind(on_release=self.on_logins_button_click)
        personal_button.bind(on_release=self.on_personal_button_click)
        history_button.bind(on_release=self.on_history_button_click)
        trash_button.bind(on_release=self.on_trash_button_click)

        
        self.add_widget(all_items_button)
        self.add_widget(logins_button)
        self.add_widget(personal_button)
        self.add_widget(history_button)
        self.add_widget(trash_button)

    def on_all_items_button_click(self, instance):
        self.app.switch_to_login()

    def on_logins_button_click(self, instance):
        pass

    def on_personal_button_click(self, instance):
        pass

    def on_history_button_click(self, instance):
        pass

    def on_trash_button_click(self, instance):
        pass
class PassLockApp(MDApp):
    def build(self):
        self.login_page = LoginPage()
        self.create_account_page = CreateAccountPage()
        self.sidebar_page = SidebarPage()
        return self.login_page

    def switch_to_login(self):
        self.root.clear_widgets()
        self.root.add_widget(self.login_page)

    def switch_to_create_account(self):
        self.root.clear_widgets()
        self.root.add_widget(self.create_account_page)

    def switch_to_sidebar(self):
        self.root.clear_widgets()
        self.root.add_widget(self.sidebar_page)

PassLockApp().run()
