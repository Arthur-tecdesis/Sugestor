from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
import random

# Cores personalizadas
COR_FUNDO = (94/255, 5/255, 30/255, 1)    # Vinho escuro (#5e051e)
COR_TEXTO = (212/255, 6/255, 75/255, 1)   # Rosa vibrante (#d4064b)
COR_BOTAO = (1, 1, 1, 1)                  # Branco (#ffffff)

# Lista de filmes com anos de lançamento
FILMES = [
    {"nome": "Matrix", "ano": 1999},
    {"nome": "Toy Story", "ano": 1995},
    {"nome": "Avatar", "ano": 2009},
    {"nome": "O Rei Leão", "ano": 1994},
    {"nome": "Homem-Aranha", "ano": 2002},
    {"nome": "Interestelar", "ano": 2014},
    {"nome": "Coringa", "ano": 2019},
    {"nome": "Os Vingadores", "ano": 2012},
    {"nome": "Titanic", "ano": 1997},
    {"nome": "O Poderoso Chefão", "ano": 1972}
]

class FilmeApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Fundo colorido
        with layout.canvas.before:
            Color(*COR_FUNDO)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        
        # Atualizar fundo ao redimensionar
        layout.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)
        
        # Título
        titulo = Label(
            text="Sugestor de Filmes", 
            font_size=24, 
            bold=True, 
            color=COR_TEXTO
        )
        layout.add_widget(titulo)
        
        # Campo de nome
        self.campo_nome = TextInput(
            hint_text="Digite seu nome", 
            size_hint=(1, None), 
            height=50,
            foreground_color=COR_TEXTO, 
            background_color=(1, 1, 1, 0.9)
        )
        layout.add_widget(self.campo_nome)
        
        # Botão de sugestão
        botao = Button(
            text="Sugerir Filme", 
            size_hint=(1, None), 
            height=50,
            background_color=COR_BOTAO,  # Botão branco
            color=COR_FUNDO,             # Texto do botão na cor de fundo
            bold=True
        )
        botao.bind(on_press=self.sugerir_filme)
        layout.add_widget(botao)
        
        # Mensagem de sugestão
        self.label_sugestao = Label(
            text="", 
            color=COR_TEXTO, 
            font_size=20
        )
        layout.add_widget(self.label_sugestao)
        
        # Mensagem adicional
        self.label_extra = Label(
            text="", 
            color=COR_TEXTO, 
            font_size=16,
            italic=True
        )
        layout.add_widget(self.label_extra)
        
        # Mensagem de erro (inicialmente vazia)
        self.label_erro = Label(
            text="", 
            color=(1, 1, 1, 1), # Branco
            font_size=16
        )
        layout.add_widget(self.label_erro)
        
        return layout

    def atualizar_fundo(self, instance, value):
        # Atualiza o fundo quando a janela é redimensionada
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def sugerir_filme(self, instance):
        # Limpa mensagens anteriores
        self.label_erro.text = ""
        self.label_sugestao.text = ""
        self.label_extra.text = ""
        
        # Obtém o nome digitado
        nome = self.campo_nome.text.strip()
        
        # Verifica se o nome foi preenchido
        if not nome:
            self.label_erro.text = "Erro: preencha os dados acima para poder continuar"
            return
        
        # Verifica se o nome contém apenas números
        if nome.isdigit():
            self.label_erro.text = "Erro: por favor coloque seu nome ao invés de números"
            return
        
        # Seleciona um filme aleatório
        filme = random.choice(FILMES)
        
        # Exibe a sugestão
        self.label_sugestao.text = f"Olá, {nome}! Sua sugestão de filme é: {filme['nome']} ({filme['ano']})."
        self.label_extra.text = "Acho que você possa gostar desse filme!"

if __name__ == '__main__':
    FilmeApp().run()