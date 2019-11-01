import requests
import json

url = 'localhost'
port = '8080'

get = requests.get('http://'+url+':'+port+'/chaves/')
nfces = get.json()

def put():
	for nfce in nfces:
		put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': nfce})
		print(put.json())


