from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button


class NumberInput(TextInput):
    pass


class NumberOption(GridLayout):
    pass


# --------- TOGGLE OPTION START ---------------------
class BinOption(ToggleButton):
    pass


class OctOption(ToggleButton):
    pass


class DecOption(ToggleButton):
    pass


class HexOption(ToggleButton):
    pass


# --------- TOGGLE OPTION END ---------------------
class ConvertResult(GridLayout):
    pass


class CalculatorConverter(GridLayout):
    pass


class ConverterApp(App):
    def build(self):
        return CalculatorConverter()


if __name__ == '__main__':
    ConverterApp().run()
