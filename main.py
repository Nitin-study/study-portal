from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class StudyPortalApp(App):
    def build(self):
        root = ScrollView(size_hint=(1, 1))
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text="[b]Master AI Study Portal[/b]", markup=True, font_size='24sp', size_hint_y=None, height=50))
        layout.add_widget(Button(text="AI Tutor", size_hint_y=None, height=50))
        layout.add_widget(Button(text="Doubt Resolution", size_hint_y=None, height=50))
        layout.add_widget(Button(text="Unlock Pro", background_color=(0, 0.7, 0.3, 1), size_hint_y=None, height=50))

        root.add_widget(layout)
        return root

if __name__ == '__main__':
    StudyPortalApp().run()
