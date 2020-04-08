import fileinput
import json

def prod_type(n):
    return f'Product_Type_{n}'

def prod_ct(n):
    return f'Units_{n}'

for line in fileinput.input():
    as_json = json.loads(line)
    for n in range(5):
        if as_json.get(prod_type(n)) and as_json.get(prod_ct(n)):
            data = {
                    "product": as_json.get(prod_type(n)),
                    "ct": float(as_json.get(prod_ct(n)))
            }
            print(json.dumps(data))
    
