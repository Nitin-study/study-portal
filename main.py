from kivy.app import App
from kivy.uix.label import Label

class MasterAIApp(App):
    def build(self):
        return Label(text='Welcome to Master AI Study Portal')

if __name__ == '__main__':
    MasterAIApp().run()
