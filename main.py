from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty


class CalculatorConverter(GridLayout):
    """
    Class CalculatorConverter
    =========================
    Kelas ini yang akan menjadi layout utama pada Applikasi. diantara layout yang tersedia
    kita akan menggunakan GridLayout karena mudah diatur seperti layouting table ada row dan
    kolom. juga disini ada default variable dan variable initial pada Class Layout kita.
    """

    # variable default dan input variable dari TextInput Kivy.
    input_type      = 2
    input_value     = NumericProperty()

    # hasil output dari konverter, tetapi di deklarasi sebagai tipe String
    binary_result  = StringProperty()
    octal_result   = StringProperty()
    decimal_result = StringProperty()
    hexa_result    = StringProperty()

    def converting(self, value):
        """
        def converting
        ==============
        fungsi ini akan merubah input dari user menjadi keluaran yang telah di konversi
        sesuai dengan tipe konversi input, beberapa diantaranya me-representasikan
        - 2 = biner, 8 = oktal, 10 = desimal, 16 = hexadesimal bilangan ini diambil
        dari jumlah byte yang tertera pada input lalu tiap fungsi ini ke-trigger
        maka akan mengkonversi hasil.
        ==============
        :param value:
        :return:
        """
        if self.input_type in [2, 8, 10, 16]:
            try:
                d = int(str(value), self.input_type)

            except ValueError:
                # Kalo valuenya gak sesuai maka di biarin aja
                pass

            else:
                # Yang paling penting itu kita ubah dulu ke desimal
                # sisanya kita bisa format dengan python.
                self.decimal_result = str(d)
                self.binary_result  = '{:0b}'.format(d)
                self.octal_result   = '{:0o}'.format(d)
                self.hexa_result    = '{:0x}'.format(d)


class ConverterApp(App):
    def build(self):
        return CalculatorConverter()


if __name__ == '__main__':
    ConverterApp().run()
