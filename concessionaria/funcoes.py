from conexao import conectar
def cadastrar(frota):
    while True:
        veiculo = {}
        veiculo['NOME'] =     input('Infome o nome do veiculo: ')
        veiculo['ANO'] = int(input('Informe o ano: ')) 
        veiculo['VALOR'] = float(input('Informe o valor: R$  '))
        veiculo['DESCRIÇÃO'] = input('Informe a descrição: ')
        veiculo['KM'] = input('OKM OU USADO: ')
        print('_'*50)
        
        con = conectar()
        cursor = con.cursor()

        sql = """Insert into veiculo
        (nome, valor, descricao, tipo) values (%s,%s,%s,%s)"""

        cursor.execute(sql,(veiculo['NOME'], veiculo['VALOR'], veiculo['DESCRIÇÃO'], veiculo['KM'],))
        con.commit()

        r = input('Deseja continuar (S/N) ? ').lower()
        if r == 'n':
            print('_'*50)
            break

"""
def listar(frota):
    for c in frota:
        for k, v in c.items():
            print(f"{k}: {v}")
        print('_'*50)
"""

def marca(frota):
    while True:
        marca={}    
        marca['MARCA']=input('Marca do veículo: ')
        
        con = conectar()
        cursor = con.cursor()
        print('_'*50)

        sql = 'Insert into marca (nome) values (%s)'

        cursor.execute(sql, (marca['MARCA'],))
        con.commit()

        r = input('Deseja continuar (S/N) ? ').lower()
        if r == 'n':
            print('_'*50)
            break

def listarVeiculos(frota):
    con = conectar()
    cursor = con.cursor()

    sql = 'select * from veiculo order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for v in resultado:
        print(v)

def listarMarca(frota):
    con = conectar()
    cursor = con.cursor()

    sql = 'select * from marca order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for m in resultado:
        print(m)
    
def cadastrarCliente(frota):
    con = conectar()
    cursor = con.cursor()

    sql = 'select * from marca order by nome'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for c in resultado:
        print(c)
'''
::outra forma do listar::
for contato in frota:
    print(f"Nome: {contato['NOME']} - Valor: R$ {contato['VALOR']} - Ano: {contato['ANO']} - DESCRIÇÃO: {contato['DESCRIÇÃO']} - KM:{contato['KM']} ")
    print('_'*50)
'''
