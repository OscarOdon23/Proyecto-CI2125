import csv
import random
import time
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.label import Label
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.utils import get_color_from_hex

class SimulateParcialMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()
        self.parcial_selected = False

    def create_widgets(self):
        layout = GridLayout(cols=1, padding=10)
        self.add_widget(layout)
        layout.add_widget(Label(text='Simular Parcial', color=get_color_from_hex('#FFFFFF')))
        layout.add_widget(Button(text='Parcial 1', on_release=self.start_parcial1, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 2', on_release=self.start_parcial2, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 3', on_release=self.start_parcial3, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Regresar al menú', on_release=self.go_menu, background_color=get_color_from_hex('#9E9E9E')))

    def start_parcial1(self, instance):
        self.parcial_selected = True
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 1
        self.manager.add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def start_parcial2(self, instance):
        self.parcial_selected = True
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 2
        self.manager.add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def start_parcial3(self, instance):
        self.parcial_selected = True
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 3
        self.manager.add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def go_menu(self, instance):
        self.manager.current = 'menu_screen'


class TheoreticalSummaryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()

    def create_widgets(self):
        layout = GridLayout(cols=1, padding=10)
        self.add_widget(layout)
        layout.add_widget(Label(text='Resumen Teórico', color=get_color_from_hex('#FFFFFF')))
        layout.add_widget(Button(text='Parcial 1', on_release=self.parcial1, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 2', on_release=self.parcial2, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 3', on_release=self.parcial3, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Regresar al menú', on_release=self.go_menu, background_color=get_color_from_hex('#9E9E9E')))

    def parcial1(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 1
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def parcial2(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 2
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'
   
    def parcial3(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 3
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def go_menu(self, instance):
        self.manager.current = 'menu_screen'

class EquationSummaryMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()

    def create_widgets(self):
        layout = GridLayout(cols=1, padding=10)
        self.add_widget(layout)
        layout.add_widget(Label(text='Resumen de Ecuaciones', color=get_color_from_hex('#FFFFFF')))
        layout.add_widget(Button(text='Parcial 1', on_release=self.parcial1, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 2', on_release=self.parcial2, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 3', on_release=self.parcial3, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Regresar al menú', on_release=self.go_menu, background_color=get_color_from_hex('#9E9E9E')))

    def parcial1(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 1
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def parcial2(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 2
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'
   
    def parcial3(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 3
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def go_menu(self, instance):
        self.manager.current = 'menu_screen'

class PracticeSubmenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()

    def create_widgets(self):
        layout = GridLayout(cols=1, padding=10)
        self.add_widget(layout)
        layout.add_widget(Label(text='Simular Parcial', color=get_color_from_hex('#FFFFFF')))
        layout.add_widget(Button(text='Parcial 1', on_release=self.parcial1, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 2', on_release=self.parcial2, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Parcial 3', on_release=self.parcial3, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Regresar al menú', on_release=self.go_menu, background_color=get_color_from_hex('#9E9E9E')))

    def parcial1(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 1
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def parcial2(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 2
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'
   
    def parcial3(self, instance):
        parcial_screen = SimulateParcialScreen(name='simulate_parcial_screen')
        parcial_screen.parcial_number = 3
        self.manager.get_screen('simulate_parcial_screen').add_widget(parcial_screen)
        self.manager.current = 'simulate_parcial_screen'

    def go_menu(self, instance):
        self.manager.current = 'menu_screen'

class TestingPhysics(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(SimulateParcialMenuScreen(name='simulate_parcial_menu_screen'))
        sm.add_widget(TheoreticalSummaryScreen(name='theoretical_summary_screen'))
        sm.add_widget(EquationSummaryMenuScreen(name='equation_summary_menu_screen'))
        sm.add_widget(PracticeSubmenuScreen(name='practice_submenu_screen'))
        return sm

    def on_start(self):
        self.root.current = 'menu_screen'
        
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_widgets()

    def create_widgets(self):
        layout = GridLayout(cols=1, padding=10)
        self.add_widget(layout)
        layout.add_widget(Button(text='Simular Parcial', on_release=self.simulate_parcial_menu, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Resumen Teórico', on_release=self.resumen_teorico, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Resumen de Ecuaciones', on_release=self.resumen_ecuaciones, background_color=get_color_from_hex('#4af00e')))
        layout.add_widget(Button(text='Practica', on_release=self.practice, background_color=get_color_from_hex('#4af00e')))

    def simulate_parcial_menu(self, instance):
        self.manager.current = 'simulate_parcial_menu_screen'

    def resumen_teorico(self, instance):
        theoretical_screen = TheoreticalSummaryScreen(name='theoretical_summary_screen')
        theoretical_screen.manager = self.manager
        self.manager.get_screen('theoretical_summary_screen').add_widget(theoretical_screen)
        self.manager.current = 'theoretical_summary_screen'

    def resumen_ecuaciones(self, instance):
        equation_menu_screen = EquationSummaryMenuScreen(name='equation_summary_menu_screen')
        equation_menu_screen.manager = self.manager
        self.manager.get_screen('equation_summary_menu_screen').add_widget(equation_menu_screen)
        self.manager.current = 'equation_summary_menu_screen'

    def practice(self, instance):
        submenu_screen = PracticeSubmenuScreen(name='practice_submenu_screen')
        submenu_screen.manager = self.manager
        self.manager.get_screen('practice_submenu_screen').add_widget(submenu_screen)
        self.manager.current = 'practice_submenu_screen'

class SimulateParcialScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.parcial_number = 0
        self.questions = []
        self.current_question = 0
        self.correct_answers = 0
        self.timer = 7200  # 2 horas en segundos
        self.create_widgets()
        self.load_questions()

    def create_widgets(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        self.add_widget(layout)
        self.question_label = Label(text='', color=get_color_from_hex('#FFFFFF'), size_hint_y=0.2)
        layout.add_widget(self.question_label)
        self.options_layout = BoxLayout(orientation='vertical', spacing=10)
        layout.add_widget(ScrollView(size_hint=(1, 0.6), do_scroll_x=False))
        layout.children[1].add_widget(self.options_layout)
        self.progress_bar = ProgressBar(max=5, value=self.current_question + 1, size_hint_y=0.1)
        layout.add_widget(self.progress_bar)
        self.timer_label = Label(text='', color=get_color_from_hex('#FFFFFF'), size_hint_y=0.1)
        layout.add_widget(self.timer_label)
        self.next_button = Button(text='Siguiente', on_release=self.next_question, background_color=get_color_from_hex('#4af00e'), size_hint_y=0.1)
        layout.add_widget(self.next_button)
        self.submit_button = Button(text='Entregar', on_release=self.submit_exam, background_color=get_color_from_hex('#9E9E9E'), size_hint_y=0.1)
        layout.add_widget(self.submit_button)

    def load_questions(self):
        filename = f'parcial{self.parcial_number}.csv'
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Ignorar encabezados
            self.questions = list(csv_reader)

    def update_question(self):
        question = self.questions[self.current_question]
        self.question_label.text = f'{question[0]}\n\nPuntaje: 6 puntos'
        self.options_layout.clear_widgets()
        for i in range(1, 6):
            checkbox = CheckBox(group='options')
            checkbox.option_index = i
            self.options_layout.add_widget(checkbox)
            self.options_layout.add_widget(Label(text=question[i]))

    def next_question(self, instance):
        if self.current_question < 4:
            self.current_question += 1
            self.update_question()
            self.progress_bar.value = self.current_question + 1
        else:
            self.submit_exam(instance)

    def submit_exam(self, instance):
        self.calculate_score()
        self.show_results()

    def calculate_score(self):
        question = self.questions[self.current_question]
        selected_option = None
        for child in self.options_layout.children:
            if isinstance(child, CheckBox) and child.active:
                selected_option = child.option_index
                break
        if selected_option == int(question[6]):
            self.correct_answers += 1

    def show_results(self):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup = Popup(title='Resultados', content=popup_layout, size_hint=(0.8, 0.8))
        popup_layout.add_widget(Label(text=f'Preguntas correctas: {self.correct_answers}/5', color=get_color_from_hex('#FFFFFF')))
        if self.correct_answers < 5:
            popup_layout.add_widget(Label(text='Respuestas incorrectas:', color=get_color_from_hex('#FFFFFF')))
            for index, question in enumerate(self.questions):
                if int(question[6]) != index + 1:
                    popup_layout.add_widget(Label(text=question[0], color=get_color_from_hex('#FFFFFF')))
                    popup_layout.add_widget(Button(text='Ver procedimiento', on_release=self.show_procedure(question[7])))
        popup.open()

    def show_procedure(self, procedure_path):
        def open_pdf(instance):
            try:
                c = canvas.Canvas("procedure.pdf", pagesize=letter)
                c.drawString(100, 750, "Procedimiento:")
                with open(procedure_path, 'r') as file:
                    procedure_text = file.read()
                    c.drawString(100, 700, procedure_text)
                c.save()
                import os
                os.startfile("procedure.pdf")
            except Exception as e:
                print(e)

        return open_pdf

    def start_timer(self):
        while self.timer > 0:
            time.sleep(1)
            self.timer -= 1
            self.timer_label.text = f'Tiempo restante: {self.timer // 3600}:{(self.timer % 3600) // 60}:{self.timer % 60}'
        self.submit_exam(None)

if __name__ == '__main__':
    TestingPhysics().run()