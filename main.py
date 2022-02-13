"""
@autor: Boubacar Sow
@date: 08/02/2022

"""
from kivy.lang import Builder
from ordonnanceur_app import MainWidget
from kivy.app import App
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager


Builder.load_file("ordonnanceur_app.kv")


class MyScreenManager(NavigationScreenManager):
    pass

class OrdApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


if __name__ == '__main__':
    OrdApp().run()
