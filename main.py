from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.config import Config
from kivy.metrics import dp
import pyperclip
import convertor
import sys
import os

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class KeySwitchApp(App):
    def build(self):
        self.icon=self.resource_path("img/logo.png")
        self.replace_languages_counter = 0
        self.mode = 0
        self.main_layout = FloatLayout()
        self.bg_image = Image(source=self.resource_path('img/bg.png'),
                              size_hint=(1, 1),
                              pos_hint={'x': 0, 'y': 0},
                              allow_stretch=True,
                              keep_ratio=False)
        self.main_layout.add_widget(self.bg_image)
        #main_screen
        self.main_screen = FloatLayout()
        self.main_screen_replace_button = Button(text ='< >',
                                                 background_normal=self.resource_path('img/btn.png'),
                                                 background_down=self.resource_path('img/btn.png'),
                                                 size_hint=(.2, .08),
                                                 pos_hint={'x': .4, 'y':.9},
                                                 font_size=dp(15),
                                                 color=(1, 1, 1, 1),
                                                 on_release=self.replace_languages)
        self.main_screen_eng_button = Button(text ='eng',
                                                 size_hint=(.2, .08),
                                                 pos_hint={'x': .01, 'y':.9},
                                                 background_normal=self.resource_path('img/btn.png'),
                                                 background_down=self.resource_path('img/btn.png'),
                                                 font_size=dp(15),
                                                 color=(1, 1, 1, 1))
        self.main_screen_ua_button = Button(text ='ua',
                                                 size_hint=(.2, .08),
                                                 pos_hint={'x': .79, 'y':.9},
                                                 background_normal=self.resource_path('img/btn.png'),
                                                 background_down=self.resource_path('img/btn.png'),
                                                 font_size=dp(15),
                                                 color=(1, 1, 1, 1))
        self.main_screen_base_text_textinput = TextInput(text='',
                                                    hint_text='english...',
                                                     size_hint=(.98, .4),
                                                     pos_hint={'x': .01, 'y': .5},
                                                     background_color=(0, 0, 0, .5),
                                                     foreground_color=(1, 1, 1, 1),
                                                     cursor_color=(1, 0, 0, 1),
                                                     font_size=dp(15),
                                                     multiline=True)
        self.main_screen_convert_and_copy_button = Button(text ='convert and copy result',
                                                 size_hint=(.98, .08),
                                                 pos_hint={'x': .01, 'y':.41},
                                                 background_color=(0, 1, 0, .5),
                                                 font_size=dp(15),
                                                 color=(1, 1, 1, 1),
                                                 on_release=self.convert)
        self.main_screen_converted_text_textinput = TextInput(text='',
                                                    hint_text='ukrainian...',
                                                     size_hint=(.98, .4),
                                                     pos_hint={'x': .01, 'y': .01},
                                                     background_color=(0, 0, 0, .5),
                                                     foreground_color=(1, 1, 1, 1),
                                                     cursor_color=(1, 0, 0, 1),
                                                     font_size=dp(15),
                                                     multiline=True)
        for widget in [
            self.main_screen_base_text_textinput,
            self.main_screen_converted_text_textinput,
            self.main_screen_convert_and_copy_button,
            self.main_screen_replace_button,
            self.main_screen_eng_button,
            self.main_screen_ua_button
        ]:
            self.main_screen.add_widget(widget)
        self.main_layout.add_widget(self.main_screen)
        return self.main_layout

    def replace_languages(self, instance):
        self.main_screen_base_text_textinput.text=""
        self.main_screen_converted_text_textinput.text=""
        if self.replace_languages_counter % 2 == 0:
            self.main_screen_eng_button.pos_hint={'x': .79, 'y':.9}
            self.main_screen_ua_button.pos_hint={'x': .01, 'y':.9}
            self.main_screen_base_text_textinput.hint_text="ukrainian..."
            self.main_screen_converted_text_textinput.hint_text = "english..."
            self.mode = 1
        else:
            self.main_screen_eng_button.pos_hint={'x': .01, 'y':.9}
            self.main_screen_ua_button.pos_hint={'x': .79, 'y':.9}
            self.main_screen_base_text_textinput.hint_text = "english..."
            self.main_screen_converted_text_textinput.hint_text = "ukrainian..."
            self.mode = 0
        self.replace_languages_counter += 1
    def convert(self, instance):
        self.main_screen_converted_text_textinput.text = str(convertor.get_text(str(self.main_screen_base_text_textinput.text), str(self.mode)))
        pyperclip.copy(self.main_screen_converted_text_textinput.text)
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
            # print('it was MEIPASS...')
        except Exception:
            base_path = os.path.abspath(".")
        # print(os.path.join(base_path, relative_path))
        return os.path.join(base_path, relative_path)








KeySwitchApp().run()

