from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="Adicionar Fundos",
    font_size="28sp",
    size_hint=(1, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .8}
))

floatlayout.add_widget(Label(
    text="Nome: ",
    font_size="20sp",
    size_hint=(.4, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .6}
))

floatlayout.add_widget(Label(
    text="Data:",
    font_size="20sp",
    size_hint=(.4, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .459}
))

floatlayout.add_widget(Label(
    text="Valor:",
    font_size="20sp",
    size_hint=(.4, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .30}
))

floatlayout.add_widget(Label(
    text="Renda fixa:",
    font_size="20sp",
    size_hint=(.5, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .20}
))

txt_nome = TextInput(
    multiline=False,
    size_hint=(0.6, .05),
    pos_hint={'x': .3, 'y': .623}
)

spn_dia = Spinner(
    text="Dia",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .30, 'y': .485}
)

spn_mes = Spinner(
    text="Mes",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .47, 'y': .485}
)

spn_ano = Spinner(
    text="Ano",
    size_hint=(0.2, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .64, 'y': .485}
)

txt_valor = TextInput(
    multiline=False,
    input_type='number',
    size_hint=(0.3, .05),
    pos_hint={'x': .3, 'y': .325}
)

renda_fix = CheckBox(
    size_hint=(0.27, .04),
    pos_hint={'x': .35, 'y': .23}
)

btn = Button(
    text="OK",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn1 = Button(
    text="Voltar",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

floatlayout.add_widget(txt_nome)
floatlayout.add_widget(txt_valor)
floatlayout.add_widget(spn_dia)
floatlayout.add_widget(spn_mes)
floatlayout.add_widget(spn_ano)
floatlayout.add_widget(renda_fix)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
