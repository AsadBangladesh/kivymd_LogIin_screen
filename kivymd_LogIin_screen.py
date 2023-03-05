from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:
    MDCard:
        size_hint: None, None
        size: 600, 800
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        padding: 25
        spacing: 25
        elevation: 10
        orientation: 'vertical'

        MDLabel:
            id: welcome_label
            text: "Welcom"
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

    
        MDTextField:
            id: username
            hint_text: "username"
            icon_right: "account"
            size_hint_x: None
            width: 500
            fond_size: 18
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: password
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 500
            fond_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

        MDRoundFlatButton:
            text: "Login"
            font_size: 25
            pos_hint: {"center_x": 0.5}
            on_press: app.logger()

        MDRoundFlatButton:
            text: "Clear"
            font_size: 25
            pos_hint: {"center_x": 0.5}
            on_press: app.clear()
        
        Widget:
            size_hint_y: None
            height: 50

'''

class LoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)

    def logger(self):
        self.root.ids.welcome_label.text = f'Input {self.root.ids.username.text}!'
    def clear(self):
        self.root.ids.welcome_label.text = "Welcom"
        self.root.ids.username.text = ""
        self.root.ids.password.text = ""

LoginApp().run()