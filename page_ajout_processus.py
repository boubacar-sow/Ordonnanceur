from kivy.lang import Builder

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from navigation_screen_manager import NavigationScreenManager

Builder.load_file("page_ajout_processus.kv")


class PageAjoutProcessus(GridLayout):
    nom_processus = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Nom du processus: ", size_hint_y=None, height=30, size_hint_x=None, width=250))
        self.process_name = TextInput(multiline=False, size_hint_y=None, height=30, size_hint_x=None, width=200)
        self.add_widget(self.process_name)

        self.add_widget(Label(text="Priorité: ", size_hint_y=None, height=30, size_hint_x=None, width=250))
        self.process_priority = TextInput(text='0', multiline=False, size_hint_y=None, height=30, size_hint_x=None,
                                          width=100)
        self.add_widget(self.process_priority)

        self.add_widget(Label(text="Nombre de threads: ", size_hint_y=None, height=30, size_hint_x=None, width=250))
        self.process_thread_number = TextInput(text='0', multiline=False, size_hint_y=None, height=30, size_hint_x=None,
                                               width=100)
        self.add_widget(self.process_thread_number)

        self.add_widget(
            Label(text="Nombre d'instructions de calcul: ", size_hint_y=None, height=30, size_hint_x=None, width=250))
        self.process_instruct_number = TextInput(text='0', multiline=False, size_hint_y=None, height=30,
                                                 size_hint_x=None, width=100)
        self.add_widget(self.process_instruct_number)

        self.add_widget(
            Label(text="Nombre d'instructions d'entrée/sortie: ", size_hint_y=None, height=30, size_hint_x=None,
                  width=260))
        self.process_instruct_io_number = TextInput(text='0', multiline=False, size_hint_y=None, height=30,
                                                    size_hint_x=None, width=100)
        self.add_widget(self.process_instruct_io_number)

        self.add_widget(
            Label(text="Nombre de cycles avant initialisation: ", size_hint_y=None, height=30, size_hint_x=None,
                  width=260))
        self.process_cycle_number_before_init = TextInput(text='0', multiline=False, size_hint_y=None, height=30,
                                                          size_hint_x=None, width=100)
        self.add_widget(self.process_cycle_number_before_init)

    def send_informations(self):
        process_name = self.process_name
        process_priority = self.process_priority
        process_thread_number = self.process_thread_number
        process_instruct_number = self.process_instruct_number
        process_instruct_io_number = self.process_instruct_io_number
        process_cycle_number_before_init = self.process_cycle_number_before_init

        return process_name, process_priority, process_thread_number, process_instruct_number, process_instruct_io_number, process_cycle_number_before_init
