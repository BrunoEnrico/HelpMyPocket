import sqlite3


def cria_banco():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE usuario(nome TEXT NOT NULL, saldo_atual REAL NOT NULL);")
    cursor.execute("CREATE TABLE movimentos (categoria TEXT NOT NULL, descricao TEXT NOT NULL, valor REAL NOT NULL,"
                   "data TEXT NOT NULL, desp_fixa INTEGER)")
    conn.commit()
    cursor.close()


def inserir_usuario(nome_usuario, saldo_atual):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO usuario(nome, saldo_atual)"
                   "VALUES('" + nome_usuario + "', '" + str(saldo_atual) + "');")
    conn.commit()
    cursor.close()


def consulta_saldo():
    resultados = {"saldo": "", "total_gastos": "", "maior_gasto": ""}
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT saldo_atual FROM usuario")
    saldo = cursor.fetchall()[0]
    total_gastos = []
    cursor.execute("SELECT valor FROM movimentos WHERE categoria = 'g' ORDER BY valor DESC")
    rows = cursor.fetchall()
    for i in rows:
        total_gastos.append(i[0])
    resultados["saldo"] = saldo[0]
    resultados["total_gastos"] = total_gastos
    try:
        resultados["maior_gasto"] = rows[0][0]
    except:
        pass
    cursor.close()
    return resultados


def consulta_movimento():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, descricao, valor, data, categoria FROM movimentos")
    movimentos = cursor.fetchall()
    return movimentos


def select_preenche_edit(rowid):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, descricao, valor, data, desp_fixa FROM movimentos WHERE rowid = " + str(rowid))
    movimentos = cursor.fetchall()
    return movimentos


def edita_gasto(rowid, nome, valor, data, desp_fix):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE movimentos SET descricao = '" + nome + "', valor = " + str(valor) + ","
                   " data = '" + data + "', desp_fixa = " + str(desp_fix) + " WHERE rowid = " + str(rowid))
    conn.commit()
    conn.close()


def pesquisa_movimentos(pesquisa):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, descricao, valor, data , categoria FROM movimentos WHERE descricao = '" + pesquisa + "'")
    movimentos = cursor.fetchall()
    return movimentos


def excluir_gasto(rowid):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT categoria, valor FROM movimentos WHERE rowid = '" + str(rowid) + "'")
    result = cursor.fetchall()
    categoria = result[0][0]
    valor = result[0][1]
    cursor.execute("SELECT saldo_atual FROM usuario")
    saldo_atual = cursor.fetchall()[0][0]
    if categoria == "f":
         novo_saldo = saldo_atual - float(valor)
    else:
        novo_saldo = saldo_atual + float(valor)
    cursor.execute("UPDATE usuario SET saldo_atual = " + str(novo_saldo))
    cursor.execute("DELETE FROM movimentos WHERE rowid = '" + str(rowid) + "'")
    conn.commit()
    conn.close()


def insere_gasto(nome, valor, data, desp_fix):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO movimentos(categoria, descricao, valor, data, desp_fixa)"
                   "VALUES('g', '" + nome + "', " + str(valor) + ", '" + data + "', " + str(desp_fix) + ")")
    cursor.execute("SELECT saldo_atual FROM usuario")
    saldo_atual = cursor.fetchall()[0][0]
    novo_saldo = saldo_atual - float(valor)
    cursor.execute("UPDATE usuario SET saldo_atual = " + str(novo_saldo))
    conn.commit()
    conn.close()


def adiciona_fundos(nome, valor, data):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO movimentos(categoria, descricao, valor, data)"
                   "VALUES('f', '" + nome + "', " + str(valor) + ", '" + data + "')")

    cursor.execute("SELECT saldo_atual FROM usuario")
    saldo_atual = cursor.fetchall()[0][0]
    novo_saldo = saldo_atual + float(valor)
    cursor.execute("UPDATE usuario SET saldo_atual = " + str(novo_saldo))

    conn.commit()
    conn.close()


