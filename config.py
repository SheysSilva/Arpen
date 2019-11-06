import requests
import json

url = '10.0.25.16'
port = '8080'

def getAll():
	get = requests.get('http://'+url+':'+port+'/chaves/')
	return get.json()

def setStatus(id, status):
	put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': id, 'status': str(status)})
	print(put.json())

def deletAll():
	delete = requests.delete('http://'+url+':'+port+'/chaves/')
	print(delete.json())

def delete(id):
	delete = requests.delete('http://'+url+':'+port+'/chaves/', data={'id': str(id)})
	print(delete.json())


