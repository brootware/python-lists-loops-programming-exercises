incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:
def my_var(x):
    x = x["name"] + " " + x["lastName"]
    return x

transformedData = list(map(my_var,incomingAJAXData))
print(transformedData)

