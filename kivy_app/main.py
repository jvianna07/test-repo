# Importar bibliotecas 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


# Classe de widgets 
class MyWidget(BoxLayout):
    texto = StringProperty("Hello World!")

    def atualizar_texto(self, novo_texto):
        self.texto = f"Você digitou: {novo_texto}"


# Classe principal do app 
class MyApp(App):
    def build(self):
        return MyWidget()


# Run
if __name__ == '__main__':
    MyApp().run()