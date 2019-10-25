import os
direct = 'data'
files = os.listdir(direct)
nfces = open('NFCE.txt','r')

keys = []
def verify(file, key):
	for name in file:
		key_nfce = name.split('|')[0]
		if key == key_nfce:
			return  True
	return False

final = 63
j = 0
lines = nfces.readlines()
size = len(lines)
for i in range(size):
	key = lines[i].split('|')[0]
	analize = False
	if i<=final:
		print(j)
		file = open(direct+'/'+files[j],'r')
		analize = verify(file, key)
	if i==final:
		if final == size-1 | final == size or j+1==len(files):
			break
		final+=64
		j+=1
	print(analize)
	if not(analize):
		keys.append(key)
print(keys)
