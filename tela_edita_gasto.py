from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

floatlayout = FloatLayout()


floatlayout.add_widget(Label(
    text="Editar Gastos",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x':0, 'y':.85}
))

floatlayout.add_widget(Label(
    text="Codigo: ",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .75}
))

floatlayout.add_widget(Label(
    text="Nome:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .62}
))

floatlayout.add_widget(Label(
    text="Data:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.37, .1),
    pos_hint={'x': 0, 'y': .5}
))

floatlayout.add_widget(Label(
    text="Valor:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))

floatlayout.add_widget(Label(
    text="Despesa Fixa:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.55, .1),
    pos_hint={'x': 0, 'y': .2}
))

lbl = Label(
    text="",
    font_size='20sp',
    color=(1, 1, 1, 1),
    size_hint=(0.6, .1),
    pos_hint={'x': 0, 'y': .75}
)

txt_desc = TextInput(
    size_hint=(0.5, .04),
    multiline=False,
    pos_hint={'x': .30, 'y': .65}
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
    pos_hint={'x': .35, 'y': .22}
)

btn_ok = Button(
    text="OK",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn_cancel = Button(
    text="Cancelar",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

btn_excluir = Button(
    text="Excluir gasto",
    size_hint=(0.25, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .40, 'y': .777}
)

floatlayout.add_widget(lbl)
floatlayout.add_widget(txt_desc)
floatlayout.add_widget(txt_valor)
floatlayout.add_widget(spn_dia)
floatlayout.add_widget(spn_mes)
floatlayout.add_widget(spn_ano)
floatlayout.add_widget(desp_fix)
floatlayout.add_widget(btn_ok)
floatlayout.add_widget(btn_cancel)
floatlayout.add_widget(btn_excluir)
