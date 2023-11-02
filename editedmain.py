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

        # Create widgets
        username_input = TextInput(hint_text="Enter username here")
        password_input = TextInput(hint_text="Enter password here", password=True)
        login_button = Button(text="Login")
        forgot_password_button = Button(text="Forgot Password")
        create_account_button = Button(text="Create Account")

        # Define event handlers
        login_button.bind(on_release=self.on_login_button_click)
        forgot_password_button.bind(on_release=self.on_forgot_password_button_click)
        create_account_button.bind(on_release=self.on_create_account_button_click)

        # Add widgets to the layout
        self.add_widget(username_input)
        self.add_widget(password_input)
        self.add_widget(login_button)
        self.add_widget(forgot_password_button)
        self.add_widget(create_account_button)

    def on_login_button_click(self, instance):
        # Handle the login button click
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

        # Create widgets
        username_input = TextInput(hint_text="Enter username")
        email_input = TextInput(hint_text="Enter email")
        password_input = TextInput(hint_text="Enter password", password=True)
        confirm_password_input = TextInput(hint_text="Confirm password", password=True)
        create_account_button = Button(text="Create Account")
        back_to_login_button = Button(text="Back To Login")

        # Define event handlers
        create_account_button.bind(on_release=self.on_create_account_button_click)
        back_to_login_button.bind(on_release=self.on_back_to_login_button_click)

        # Add widgets to the layout
        self.add_widget(username_input)
        self.add_widget(email_input)
        self.add_widget(password_input)
        self.add_widget(confirm_password_input)
        self.add_widget(create_account_button)
        self.add_widget(back_to_login_button)

    def on_create_account_button_click(self, instance):
        #"Create Account" button click
        username = self.children[0].text
        email = self.children[1].text
        password = self.children[2].text
        confirm_password = self.children[3].text

        # Implement your account creation logic here
        # You can validate input, create an account, and perform necessary actions

        if password == confirm_password:
            print(f"Account created for username: {username} with email: {email}")
            # You can navigate to the login page or perform other actions
            self.app.switch_to_login()
        else:
            print("Password confirmation does not match.")

    def on_back_to_login_button_click(self, instance):
        # Handle the "Back To Login" button click
        self.app.switch_to_login()
class SidebarPage(BoxLayout):
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
