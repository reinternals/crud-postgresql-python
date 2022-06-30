# - Modulo necessário para realizar as operações de CRUD no postgresql.
from psycopg2 import connect					 #pip install psycopg2

# Função - CREATE.
def fCreate():
	tabela = input('Insira o nome da tabela: ')
	empresa = 'empresa'
	departamento = 'departamento'
	funcionario = 'funcionario'

	if tabela == empresa:
		nome = input('Insira o nome da empresa: ')
		comando = f'INSERT INTO empresa (nome) VALUES ("{nome}")'
		cursor.execute(comando)
		conexao.commit()
		fContinuar()

	elif tabela == departamento:
		descricao = input('Insira a descricao: ')
		id_empresa = input('Insira o ID da empresa: ')
		comando = f'INSERT INTO departamento (descricao , id_empresa) VALUES ("{descricao}" , "{id_empresa}")'
		cursor.execute(comando)
		conexao.commit()
		fContinuar()

	elif tabela == funcionario:
		nome = input('Insira o nome do funcionario: ')
		id_departamento = input('Insira o ID do departamento: ')
		comando = f'INSERT INTO funcionario (nome , id_departamento) VALUES ("{nome}" , "{id_departamento}")'
		cursor.execute(comando)
		conexao.commit()
		fContinuar()

	else:
		print('Nome de tabela inválido!')
		fContinuar()

# Função - READ.
def fRead():
	coluna = input('Insira o nome da coluna: ')
	tabela = input('Insira o nome da tabela: ')
	comando = f'SELECT {coluna} FROM {tabela}'
	cursor.execute(comando)
	consulta = cursor.fetchall()
	print(consulta)
	fContinuar()

# função - UPDATE.
def fUpdate():
	tabela = input('Insira o nome da tabela: ')
	atributo = input('Insira o nome do atributo: ')
	vID = input('Insira o ID: ')
	vUpdate = input('Insira o novo valor: ')
	comando = f'UPDATE {tabela} SET {atributo} = "{vUpdate}" WHERE id = "{vID}"'
	cursor.execute(comando)
	conexao.commit()
	fContinuar()

# função - DELETE.
def fDelete():
	tabela = input('Insira o nome da tabela: ')
	vID = input('Insira o ID: ')
	comando = f'DELETE FROM {tabela} WHERE id = "{vID}"'
	cursor.execute(comando)
	conexao.commit()
	fContinuar()

# Função - CLOSE para finalizar a conexão com o postgresql.
def fClose():
	conexao.close()
	cursor.close()
	print('conexao encerrada com sucesso.\nBye!')
	exit()

# Função - CONTINUAR para que o usuario possa realizar outras consultas antes de finalizar o programa.
def fContinuar():
	vContinuar = input('deseja realizar outra consulta? s - sim. n - nao.')
	if vContinuar.lower() == 's':
		fMenu()
	elif vContinuar.lower() == 'n':
		fClose()
	else:
		print('Opcao invalida!')
		fContinuar()

# Função - Menu.
def fMenu():
	print('Escolha uma das opções abaixo.')
	print('1 - CREATE.\n2 - READ.\n3 - UPDATE.\n4 - DELETE.\n5 - SAIR.')
	escolha = input('Digite o numero da opcao: ')
	if escolha == '1':
		fCreate()
	elif escolha == '2':
		fRead()
	elif escolha == '3':
		fUpdate()
	elif escolha == '4':
		fDelete()
	elif escolha == '5':
		fClose()
	else:
		print('opcao invalida!')
		fContinuar()

# - Identificação do banco de dados.
conexaoID = "host='localhost' 	\
			 dbname='empresa' \
			 user='crud'	\
			 password='crud'"

# - Realiza a conexão com o postgresql.
conexao = connect(conexaoID)

# - Criação do cursor para leitura.
cursor = conexao.cursor()

# - Chamada das funções.
fMenu()