from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty


class CalculatorConverter(GridLayout):
    input_value    = NumericProperty
    input_type     = NumericProperty

    binnary_result = NumericProperty
    octal_result   = NumericProperty
    decimal_result = NumericProperty
    hexa_result    = NumericProperty

    def converting_from(self, *args):
        pass


class ConverterApp(App):
    def build(self):
        return CalculatorConverter()


if __name__ == '__main__':
    ConverterApp().run()
