from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import json

class PasS(App):
    def build(self):
        self.window = BoxLayout(orientation="vertical", spacing=10, padding=10)
        self.window.cols = 1
        self.window.size_hint =(0.6,0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        
        #All the widgets
        self.window.add_widget(Image(source ="Logo.png", size_hint=(8,8)))
        self.text_app = Label(
                            text = "No password",
                            font_size = 18
                        )
        self.window.add_widget(self.text_app)

        #App's name input
        self.app = Label(
                        text = "What is app\'s name",
                        font_size = 18
                    )
        self.window.add_widget(self.app)
        self.app_input = TextInput(
                                    multiline=False,
                                    padding_y=(20,20),
                                    size_hint = (1,0.5)
                                )
        self.window.add_widget(self.app_input)

        #Passward input
        self.passward = Label(
                                text = "What \'s the passward",
                                font_size = 18
                            )
        self.window.add_widget(self.passward)
        self.passward_input = TextInput(
                                        multiline=False,
                                        padding_y =(20,20),
                                        size_hint = (1,0.5)
                                    )
        self.window.add_widget(self.passward_input)

        #Button layout
        button_layout = BoxLayout(
            orientation = "horizontal",
            size_hint = (1,None),
            height = 50,
            spacing =10
        )

        self.submit_button = Button(
                                    text="Submit",
                                    bold = True,
                                    size_hint = (0.5,0.5)
                                )
        self.submit_button.bind(on_press=self.info)
        button_layout.add_widget(self.submit_button)
        self.display_button = Button(
                                    text="Show Passwords",
                                    size_hint = (0.5,0.5),
                                    bold = True
                                )
        self.display_button.bind(on_press=self.show)
        button_layout.add_widget(self.display_button)

        self.window.add_widget(button_layout)

        return self.window
    
    
    def load_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    
    def save_file(self,file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=3)
    
    def info(self, instance):
        login_file = self.load_file("info.json")
        app_name = self.app_input.text
        password = self.passward_input.text
        login_file["app_pass"].append({"app":app_name, "password": password})
        self.save_file("info.json", login_file)

    def login(self, instance):
        login_file = self.load_file("login.json")
        app_name = self.app_input.text
        password = self.passward_input.text
        login_file["app_pass"].append({"app":app_name, "password": password})
        self.save_file("login.json", login_file)
    def show(self, instance):
        load_file = self.load_file("info.json")
        display_text = ""
        for entry in load_file["app_pass"]:
            display_text += f"App: {entry["app"]} \nPassword: {entry["password"]}\n"
        self.text_app.text = display_text

if __name__ == "__main__":
    PasS().run()
