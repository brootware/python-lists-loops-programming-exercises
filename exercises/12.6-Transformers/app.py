incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here

def name_formatter(data:dict) -> str:
    full_name = data['name'] + ' ' + data['last_name']
    return full_name
    

def data_transformer(data_list:list) -> list:
    return list(map(name_formatter,data_list))


print(print(data_transformer(incoming_ajax_data)))