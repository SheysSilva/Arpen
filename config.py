import requests
import json

url = 'localhost'
port = '8080'

get = requests.get('http://'+url+':'+port+'/chaves/')
nfces = get.json()

def setAllStatus(status):
	for nfce in nfces:
		put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': nfce, 'status': str(status)})
		print(put.json())

def setStatus(id, status):
	put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': id, 'status': str(status)})
	print(put.json())

def deletAll():
	delete = requests.delete('http://'+url+':'+port+'/chaves/')
	print(delete.json())

def delete(id):
	delete = requests.delete('http://'+url+':'+port+'/chaves/', data={'id': str(id)})
	print(delete.json())


