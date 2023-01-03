import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='User_Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='User_Age'))
        self.s_age = TextInput()
        self.add_widget(self.s_age)

        self.add_widget(Label(text='User_gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text = 'Press the Button')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)


    def click_me(self):
        print('my User name is '+self.s_name.text)
        print('my User age is '+self.s_age.text)
        print('my User gender is '+self.s_gender.text)



class parentApp(App):
    def build(self):
        return childApp()


if __name__ == '__main__':
    parentApp().run()


