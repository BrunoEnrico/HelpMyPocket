from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="Cadastro de Gasto",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .80}
))

floatlayout.add_widget(Label(
    text="Nome:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .65}
))

floatlayout.add_widget(Label(
    text="Data:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.37, .1),
    pos_hint={'x': 0, 'y': .50}
))

floatlayout.add_widget(Label(
    text="Valor:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))

floatlayout.add_widget(Label(
    text="Despesa Fixa:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.55, .1),
    pos_hint={'x': 0, 'y': .20}
))

txt_desc = TextInput(
    size_hint=(0.5, .04),
    multiline=False,
    pos_hint={'x': .30, 'y': .68}
)

txt_valor = TextInput(
    size_hint=(0.2, .04),
    multiline=False,
    pos_hint={'x': .30, 'y': .38},
    input_type='number'
)

spn_dia = Spinner(
    text="Dia",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .30, 'y': .53}
)

spn_mes = Spinner(
    text="Mes",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .47, 'y': .53}
)

spn_ano = Spinner(
    text="Ano",
    size_hint=(0.2, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .64, 'y': .53}
)

desp_fix = CheckBox(
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

floatlayout.add_widget(txt_desc)
floatlayout.add_widget(txt_valor)
floatlayout.add_widget(spn_dia)
floatlayout.add_widget(spn_mes)
floatlayout.add_widget(spn_ano)
floatlayout.add_widget(desp_fix)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
