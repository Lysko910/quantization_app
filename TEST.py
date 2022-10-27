import json

with open('default_parameters.json', 'r') as f:
    data = json.load(f)
print(data)
parameters = {"parametr1": data['Algoritm_1'][0],
              "parametr2": data['Algoritm_1'][1],
              "parametr3": data['Algoritm_2'][0],
              "parametr4": data['Algoritm_2'][1]}

print(parameters)
