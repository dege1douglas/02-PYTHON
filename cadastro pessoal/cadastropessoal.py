import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('cadastropessoal.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://cadastro-pessoal-default-rtdb.firebaseio.com/'
})

limite = ['CADASTRO 01', 'CADASTRO 02', 'CADASTRO 03']

for x in range(len(limite)):
    print('ÁREA DE CADASTRO')
    nome = (str(input('NOME:')))
    cpf = (str(input('CPF:')))
    rg = (str(input('RG:')))
    data_nasc = (str(input('DATA DE NASCIMENTO (somente números):')))
    sexo = (str(input('SEXO:')))
    signo = (str(input('SIGNO:')))
    mainha = (str(input('NOME DA MÃE:')))
    painho = (str(input('NOME DO PAI:')))
    email = (str(input('EMAIL:')))
    senha = (str(input('DIGITE UM CÓDIGO PIN:')))
    endereco = (str(input('ENDEREÇO:')))
    cep = (str(input('CEP:')))
    numero_b = (str(input('NÚMERO:')))
    bairro = (str(input('BAIRRO:')))
    cidade = (str(input('CIDADE:')))
    estado = (str(input('ESTADO:')))
    teleco = (str(input('TELEFONE FIXO:')))
    cerelepe = (str(input('CELULAR:')))
    altura = (str(input('ALTURA:')))
    peso = (str(input('PESO:')))
    tipo_sangue = (str(input('TIPO SANGUÍNEO:')))    
    cor_fav = (str(input('COR FAVORITA:'))) 
    print("CADASTRADO COM SUCESSO!")
    ref = db.reference('/CADASTRO PESSOAL/%s'%limite[x])
    ref.set({
                'nome': nome,
                'cpf': cpf,
                'rg': rg,
                'data de nascimento': data_nasc,
                'sexo':sexo ,
                'signo': signo,
                'mae': mainha,
                'pai':painho ,
                'email': email,
                'senha': senha,
                'endereco':endereco ,
                'cep': cep,
                'numero': numero_b,
                'bairro': bairro,
                'cidade':cidade ,
                'estado': estado,
                'telefone': teleco,
                'celular':cerelepe ,
                'altura': altura,
                'peso': peso,
                'tipo sanguineo': tipo_sangue,
                'cor favorita':cor_fav,
})
mostrar = db.reference('/CADASTRO PESSOAL/pes1')
mostrar = mostrar.get()
print(mostrar(F"""Nome:{nome}
"""))