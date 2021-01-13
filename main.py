from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import funcoes_banco as fb
import tela_novo_nome as tnn
import tela_novo_valor as tnv
import tela_principal as tp
import tela_cadastra_gasto as tcg
import tela_consulta_gastos as tcgs
import tela_adicionar_fundos as taf
import tela_edita_gasto as teg
from functools import partial
import random
import os


def go_novo_valor(self):
    if tnn.txt1.text == "":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        sm.switch_to(novo_valor, direction="left")


def go_novo_gasto(self):
    sm.switch_to(novo_gasto, direction="left")


def go_adicionar_fundos(self):
    sm.switch_to(adicionar_fundos, direction="left")


def go_tela_principal(self):
    carrega_tela_principal()
    sm.switch_to(tela_principal, direction="right")


def go_consulta_gasto(self):
    carrega_consulta_gasto()
    sm.switch_to(consulta_gasto, direction="left")


def go_novo_nome(self):
    sm.switch_to(novo_nome, direction="right")


def carrega_tela_principal():
    resultado = fb.consulta_saldo()
    saldo = resultado["saldo"]
    total_gastos = 0
    try:
        maior_gasto = resultado["maior_gasto"]
    except:
        pass
    try:
        if saldo.is_integer() is False:
            saldo = round(saldo, 2)
            saldo = str(saldo)
            if len(saldo) == 5:
                saldo = saldo.replace(".", ",")
                saldo = "R$ " + saldo + "0"
            else:
                saldo = saldo.replace(".", ",")
                saldo = "R$ " + saldo
        else:
            saldo = int(saldo)
            saldo = "R$ " + str(saldo) + ",00"
    except:
        saldo = "R$ " + str(saldo) + ",00"

    for i in resultado["total_gastos"]:
        total_gastos = total_gastos + float(i)

    try:
        if total_gastos.is_integer() is False:
            total_gastos = round(total_gastos, 2)
            total_gastos = str(total_gastos)
            if len(total_gastos) == 5:
                total_gastos = total_gastos.replace(".", ",")
                total_gastos = "R$ " + total_gastos + "0"
            elif len(total_gastos) == 1:
                total_gastos = "R$ 0,00"
            else:
                total_gastos = total_gastos.replace(".", ",")
                total_gastos = "R$ " + total_gastos
        else:
            total_gastos = int(total_gastos)
            total_gastos = "R$ " + str(total_gastos) + ",00"
    except:
        total_gastos = "R$ " + str(total_gastos) + ",00"

    try:
        if maior_gasto.is_integer() is False:
            maior_gasto = str(maior_gasto)
            if len(maior_gasto) == 5:
                maior_gasto = maior_gasto.replace(".", ",")
                maior_gasto = "R$ " + maior_gasto + "0"
            else:
                maior_gasto = maior_gasto.replace(".", ",")
                maior_gasto = "R$ " + maior_gasto
        else:
            maior_gasto = int(maior_gasto)
            maior_gasto = "R$ " + str(maior_gasto) + ",00"
    except:
        maior_gasto = "R$ 0,00"

    tp.lbl_saldo.text = "Saldo atual: " + str(saldo)
    tp.lbl_total.text = "Total de gastos: " + str(total_gastos)
    tp.lbl_maior.text = "Maior gasto: " + str(maior_gasto)


def carrega_consulta_gasto():
    tcgs.gridlayout.clear_widgets()
    movimentos = fb.consulta_movimento()
    if movimentos == []:
        tcgs.gridlayout.add_widget(Label(text="Nenhum movimento encontrado!", font_size="20sp",
                                         color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:
            valor = j[2]
            try:
                if valor.is_integer() is True:
                    valor = int(valor)
                    valor = str(valor) + ",00"
            except:
                valor = str(valor) + ",00"
            if j[4] == "f":
                buttons.append(
                    Button(text="Codigo: " + str(j[0]) + "\n" + "Nome: " + j[1] + "\n" + "Valor: R$ +" + str(valor) + "\n"
                                + "Data: " + j[3], background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
            else:
                buttons.append(
                    Button(text="Codigo: " + str(j[0]) + "\n" + "Nome: " + j[1] + "\n" + "Valor: R$ -" + str(valor) + "\n"
                                + "Data: " + j[3], background_color=(1, 0, 0, 1), size_hint_y=None, height=200))
            buttons[movimentos.index(j)].bind(on_press=partial(preenche_form_edit, j))
            tcgs.gridlayout.add_widget(buttons[movimentos.index(j)])
            tcgs.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def limpa_edit_gasto(self):
    popup4.dismiss()
    go_tela_principal(self)


def preenche_form_edit(self, j):
    j = j.text
    sm.switch_to(edita_gasto)
    j = j.split('\n')
    j = j[0].split(": ")
    j = j[1]
    j = fb.select_preenche_edit(j)
    j = j[0]
    teg.lbl.text = str(j[0])
    teg.txt_desc.text = j[1]
    teg.txt_valor.text = str(j[2])
    teg.spn_dia.values = list_dia
    teg.spn_mes.values = list_mes
    teg.spn_ano.values = list_ano
    if j[4] == "1":
        teg.desp_fix.active = True
    else:
        teg.desp_fix.active = False


def exclui_gasto(self):
    rowid = teg.lbl.text
    fb.excluir_gasto(rowid)
    popup5.open()
    Clock.schedule_once(limpa_exclui_gasto, 1.5)


def atualiza_gastos(self):
    rowid = teg.lbl.text
    nome = teg.txt_desc.text
    valor = teg.txt_valor.text
    dia = teg.spn_dia.text
    mes = teg.spn_mes.text
    ano = teg.spn_ano.text
    desp_fix = teg.desp_fix.active
    if nome == "" or valor == "" or dia == "Dia" or mes == "Mes" or ano == "Ano":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        valor = valor.replace('-', '')
        mes = list_mes.index(mes)
        mes = mes + 1
        if mes < 10:
            mes = '0' + str(mes)
        data = dia + "/" + mes + "/" + ano
        if desp_fix is False:
            desp_fix = 0
        else:
            desp_fix = 1
        fb.edita_gasto(rowid, nome, valor, data, desp_fix)
        popup4.open()
        Clock.schedule_once(limpa_edit_gasto, 1.5)


def pesquisa_movimento(self):
    tcgs.gridlayout.clear_widgets()
    movimentos = str(tcgs.txt_pesquisa.text)
    movimentos = fb.pesquisa_movimentos(movimentos)
    if movimentos == []:
        tcgs.gridlayout.add_widget(Label(text="Nenhum movimento encontrado!", font_size="20sp",
                                         color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movimentos:
            valor = j[2]
            try:
                if valor.is_integer() is True:
                    valor = int(valor)
                    valor = str(valor) + ",00"
            except:
                valor = str(valor) + ",00"
            if j[4] == "f":
                buttons.append(
                    Button(text="Codigo: " + str(j[0]) + "\n" + "Nome: " + j[1] + "\n" + "Valor: R$ +" + valor + "\n"
                                + "Data: " + j[3], background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
            else:
                buttons.append(
                    Button(text="Codigo: " + str(j[0]) + "\n" + "Nome: " + j[1] + "\n" + "Valor: R$ -" + valor + "\n"
                                + "Data: " + j[3], background_color=(1, 0, 0, 1), size_hint_y=None, height=200))

            buttons[movimentos.index(j)].bind(on_press=partial(preenche_form_edit, j))
            tcgs.gridlayout.add_widget(buttons[movimentos.index(j)])
            tcgs.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def update_bar(self):
    rand = random.randint(0, 20)
    pb.value = pb.value + rand


def update():
    Clock.schedule_interval(update_bar, 0.2)


def espera_tela(self):
    popup1.dismiss()
    go_tela_principal(self)


def limpa_novo_gasto(self):
    popup2.dismiss()
    tcg.txt_desc.text = ""
    tcg.txt_valor.text = ""
    tcg.spn_dia.values = ""
    tcg.spn_dia.values = list_dia
    tcg.spn_mes.values = ""
    tcg.spn_mes.values = list_mes
    tcg.spn_ano.values = ""
    tcg.spn_ano.values = list_ano
    tcg.desp_fix.active = False


def limpa_adiciona_fundos(self):
    popup3.dismiss()
    taf.txt_nome.text = ""
    taf.txt_valor.text = ""
    taf.spn_dia.values = list_dia
    taf.spn_mes.values = list_mes
    taf.spn_ano.values = list_ano


def limpa_exclui_gasto(self):
    popup5.dismiss()
    carrega_tela_principal()
    sm.switch_to(tela_principal, direction="right")


def insere_usuario(self):
    if tnv.txt1.text == "":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        nome = tnn.txt1.text
        valor = tnv.txt1.text
        fb.inserir_usuario(nome, valor)
        popup1.open()
        for i in range(5):
            update()
        Clock.schedule_once(espera_tela, 1.5)


def insere_gasto(self):
    nome = tcg.txt_desc.text
    valor = tcg.txt_valor.text
    dia = tcg.spn_dia.text
    mes = tcg.spn_mes.text
    ano = tcg.spn_ano.text
    desp_fix = tcg.desp_fix.active
    if nome == "" or valor == "" or dia == "Dia" or mes == "Mes" or ano == "Ano":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        valor = valor.replace('-', '')
        mes = list_mes.index(mes)
        mes = mes + 1
        if mes < 10:
            mes = '0' + str(mes)
        data = dia + "/" + mes + "/" + ano
        if desp_fix is False:
            desp_fix = 0
        else:
            desp_fix = 1
        fb.insere_gasto(nome, valor, data, desp_fix)
        popup2.open()
        Clock.schedule_once(limpa_novo_gasto, 1.5)


def adiciona_fundos(self):
    nome = taf.txt_nome.text
    valor = taf.txt_valor.text
    dia = taf.spn_dia.text
    mes = taf.spn_mes.text
    ano = taf.spn_ano.text
    valor = valor.replace('-', '')
    mes = list_mes.index(mes)
    mes = mes + 1
    if mes < 10:
        mes = '0' + str(mes)
    data = dia + "/" + mes + "/" + ano
    fb.adiciona_fundos(nome, valor, data)
    popup3.open()
    Clock.schedule_once(limpa_adiciona_fundos, 1.5)


list_dia = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
            "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
list_mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
list_ano = []
for i in range(1900, 2021):
    list_ano.append(str(i))
list_ano.reverse()

sm = ScreenManager()

popup1 = Popup(title='Carregando...', size_hint=(.6, .4))
pb = ProgressBar(value=0, max=100)
popup1.add_widget(pb)

popup2 = Popup(title='Alerta!', content=Label(text="Gasto inserido\n com sucesso!"), size_hint=(.5, .2))
popup3 = Popup(title='Alerta!', content=Label(text="Fundos adicionados\n com sucesso!"), size_hint=(.5, .2))
popup4 = Popup(title='Alerta!', content=Label(text="Tudo certo! :)"), size_hint=(.5, .2))
popup5 = Popup(title='Alerta!', content=Label(text="Movimento excluido\n com sucesso! :)"), size_hint=(.5, .2))
popup_gen = Popup(title='Alerta!', content=Label(text="Campos em branco!"), size_hint=(.5, .2))


novo_nome = Screen(name="novo_nome")
novo_nome.add_widget(tnn.floatlayout)
tnn.btn.bind(on_press=go_novo_valor)

novo_valor = Screen(name="novo_valor")
novo_valor.add_widget(tnv.floatlayout)
tnv.btn.bind(on_press=insere_usuario)
tnv.btn1.bind(on_press=go_novo_nome)

tela_principal = Screen(name="tela_principal")
tela_principal.add_widget(tp.boxlayout)
tp.btn_add_fundos.bind(on_press=go_adicionar_fundos)
tp.btn_novo_gasto.bind(on_press=go_novo_gasto)
tp.btn_movimentacao.bind(on_press=go_consulta_gasto)

adicionar_fundos = Screen(name="adicionar_fundos")
adicionar_fundos.add_widget(taf.floatlayout)
taf.spn_dia.values = list_dia
taf.spn_mes.values = list_mes
taf.spn_ano.values = list_ano
taf.btn.bind(on_press=adiciona_fundos)
taf.btn1.bind(on_press=go_tela_principal)

novo_gasto = Screen(name='novo_gasto')
novo_gasto.add_widget(tcg.floatlayout)
tcg.spn_dia.values = list_dia
tcg.spn_mes.values = list_mes
tcg.spn_ano.values = list_ano
tcg.btn.bind(on_press=insere_gasto)
tcg.btn1.bind(on_press=go_tela_principal)

consulta_gasto = Screen(name='consulta_gasto')
consulta_gasto.add_widget(tcgs.floatlayout)
tcgs.btn_pesquisar.bind(on_press=pesquisa_movimento)
tcgs.btn_voltar.bind(on_press=go_tela_principal)

edita_gasto = Screen(name='edita_gasto')
edita_gasto.add_widget(teg.floatlayout)
teg.btn_ok.bind(on_press=atualiza_gastos)
teg.btn_cancel.bind(on_press=go_tela_principal)
teg.btn_excluir.bind(on_press=exclui_gasto)


if os.path.exists("database.db") is False:
    fb.cria_banco()
    sm.add_widget(novo_nome)
else:
    sm.add_widget(tela_principal)
    carrega_tela_principal()


class HelloApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 0)
        return sm


if __name__ == '__main__':
    HelloApp().run()
