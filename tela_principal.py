from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50,
    )

lbl_saldo = Label(
    text="Saldo atual: ",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(1, .05)
    )

lbl_total = Label(
    text="Total de gastos: ",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(1, .05)
    )

lbl_maior = Label(
    text="Maior gasto: R$ 0,00",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(1, .05)
    )

btn_add_fundos = Button(
    text="Adicionar Fundos",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_novo_gasto = Button(
    text="Novo Gasto",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_movimentacao = Button(
    text="Consulta de Movimentos",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

boxlayout.add_widget(lbl_saldo)
boxlayout.add_widget(lbl_total)
boxlayout.add_widget(lbl_maior)
boxlayout.add_widget(btn_add_fundos)
boxlayout.add_widget(btn_novo_gasto)
boxlayout.add_widget(btn_movimentacao)