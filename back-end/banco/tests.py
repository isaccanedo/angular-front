from django.test import TestCase
import requests
import pyautogui as pyg

#Esse módulo se destina a testar a api

#Esssa funcionalidade permite criar um usuário
def cria():
	dados = {
		'username': pyg.prompt('Usuário'),
		'password': pyg.prompt('Senha'),
		'name': pyg.prompt('Nome do usuário'),
		'email': pyg.prompt('E-mail do usuário')
	}

	url = 'http://localhost:8000/usuario/'
	requisicao = requests.post(url, data = dados)
	pyg.alert(requisicao)

#Testa a consulta de um usuario pelo id
def consulta_id():
	id = pyg.prompt('Insira o ID do usuario')

	url = f'http://localhost:8000/usuario/{id}/'
	requisicao = requests.get(url)
	pyg.alert(requisicao)
	pyg.alert(requisicao.json())

#Testa a exclusão de um usuario
def exclui():
	id = pyg.prompt('Insira o ID do usuario')

	url = f'http://localhost:8000/usuario/{id}/'
	requisicao = requests.delete(url)
	pyg.alert(requisicao)

#Verifica se um cliente existe
def login():
	dados = {
		'username': pyg.prompt('Usuário'),
		'password': pyg.prompt('Senha')
	}

	url = 'http://localhost:8000/token/'
	requisicao = requests.post(url, data = dados)
	pyg.alert(requisicao)

#Verifica se um usuario já existe e retorna um booleano (Dados para consulta: Nome do usuário)
def consulta_user():
	usuario = pyg.prompt('digite o nome do usuario')
	token = pyg.prompt('insira o token do usuario logado!')
	url = f'http://localhost:8000/usuario/existe/{usuario}/'
	cabecalho = {'Authorization': f'Bearer {token}'}
	requisicao = requests.get(url, headers=cabecalho)
	pyg.alert(requisicao.json())