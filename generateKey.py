from datetime import datetime
date = datetime.now()

models = {'NFE': 55, 'NFCE': 65,'CTE': 57}
issue_forms = {'normal': 1,'contingency1': 2,'contingency2': 3}
series = [105, 106, 124, 125]
ufs = {'PB': 25}
months = {1: '01', 2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09', 10: '10', 11: '11', 12: '12'}

def generate(cnpj, number, serie, month):
	uf = ufs['PB']
	month = months(month)
	year = date.year
	model = models['NFCE']
	number_docu = number_doc(number)
	issue_form = issue_forms['normal']
	seq = sequence(number)

	key_part = str(uf) + str(year)[2:4] + str(month) + str(cnpj) + str(model) + str(serie) + str(number_docu) + str(issue_form) + str(seq)

	div = generateDiv(key_part)
	key = key_part + str(div)
	return str(key)
	
def months(month):
	if month < 10:
		return '0' + str(month)
	return str(month)

def sequence(number):
	list = str(int(number)+1)
	seq = ''
	if len(list) < 8:
		seq = '0'*(8-len(list))
	for ch in list:
		seq += ch

	return seq

def number_doc(number):
	list = str(number)
	seq = ''
	if len(list) < 9:
		seq = '0'*(9-len(list))
	for ch in list:
		seq += ch

	return seq

def generateDiv(key):
	div = 0
	count = 2

	for i in range(len(key)-1, -1, -1):
		if count == 10:
			count = 2

		number = int(key[i])

		div += number*count
		count += 1

	res = 11-(div-(int(div/11)*11))
	if res > 9:
		return 0
	return res



