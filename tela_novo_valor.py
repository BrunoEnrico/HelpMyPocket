from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="Qual seu saldo atual?",
    font_name="minha_fonte.ttf",
    font_size='28sp',
    color=(1, 1, 1, 1),
    size_hint=(.5, .2),
    pos_hint={"x": .27, "y": .7}
))

txt1 = TextInput(
    multiline=False,
    font_size=70,
    padding_x=150,
    padding_y=8,
    input_type='number',
    size_hint=(.8, 0.07),
    pos_hint={"x": .1, "y": .5}
)

btn = Button(
    text="OK",
    background_color=(.5, 1.6, 3, .8),
    size_hint=(.5, .1),
    pos_hint={"x": .25, "y": .2}
)

btn1 = Button(
    text="Voltar",
    size_hint=(0.15, .052),
    pos_hint={'x': .05, 'y': .90},
    background_color=(.5, 1.6, 3, .8)
)

floatlayout.add_widget(txt1)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
