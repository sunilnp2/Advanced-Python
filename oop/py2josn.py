import json
print("--------------This is page where python is convert into json--------------")

dict = {
    'name':'sunil',
    'age':20,
    'p_address':'gorkha',
    't_address':'ktm',
    'qualification':'bachelor'
}

json_data = json.dumps(dict)
print(json_data)


print("--------------This is page where josn is convert into python--------------")

# when you convert json json data must inside '{}' this style

json_data = '{"name":"sunil Nepali","age":"20","p_address":"gorkha","t_address":"ktm","qualification":"bachelor" }'

python_data = json.loads(json_data)
print(python_data)