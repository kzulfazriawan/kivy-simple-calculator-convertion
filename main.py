from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty


class CalculatorConverter(GridLayout):
    '''
    CalculatorConverter
    input type, kali ini input type menggunakan angka jadi
    contohnya 1 adalah biner, 7 adalah oktal, dan 16 adalah hexa
    dan selain itu adalah desimal
    '''
    input_value    = NumericProperty
    input_type     = NumericProperty

    binnary_result = NumericProperty
    octal_result   = NumericProperty
    decimal_result = NumericProperty
    hexa_result    = NumericProperty

    def converting_from(self, *args):
        if self.input_type == 1:
            self.binnary_result = int(self.input_value, 2)

        elif self.input_type == 7:
            pass
        elif self.input_type == 16:
            pass
        else:
            pass


class ConverterApp(App):
    def build(self):
        return CalculatorConverter()


if __name__ == '__main__':
    ConverterApp().run()
