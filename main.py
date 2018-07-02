from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty


class CalculatorConverter(GridLayout):
    '''
    CalculatorConverter
    input type, kali ini input type menggunakan angka jadi
    contohnya 1 adalah biner, 7 adalah oktal, dan 16 adalah hexa
    dan selain itu adalah desimal
    '''
    input_value    = NumericProperty
    input_type     = NumericProperty

    binary_result  = StringProperty
    octal_result   = StringProperty
    decimal_result = StringProperty
    hexa_result    = StringProperty

    def converting(self, value):
        try:
            v = int(value)
        except ValueError:
            pass
        else:
            if self.input_type in [2, 8, 16]:
                d = int(str(v), self.input_type)
                self.decimal_result = str(d)
                self.binary_result = '{:0b}'.format(d)
                self.octal_result = '{:0o}'.format(d)
                self.hexa_result = '{:0x}'.format(d)

                print(self.binary_result, self.decimal_result, self.octal_result, self.hexa_result)


class ConverterApp(App):
    def build(self):
        return CalculatorConverter()


if __name__ == '__main__':
    ConverterApp().run()
