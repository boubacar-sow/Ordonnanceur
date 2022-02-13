from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from page_ajout_processus import PageAjoutProcessus


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        """self.process_informations = PageAjoutProcessus().send_informations()

        pid = 0
        label = Label(text="Nom: " + self.ids.process_informations[0].text + "\nPid: " + str(pid), size_hint=(None, None),
                      valign='top')

        self.add_widget(label)"""
