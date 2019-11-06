nfce = 'Lista Dirceu.txt'
nfces = open(nfce,'r')
summ = 0
for nfce in nfces:
	summ+=1
print(summ/64)
print(summ%64)
