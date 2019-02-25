import json

#x =  '{ "name":"John", "age":21, "city":"USA"}'
with open('text.json', 'r') as json_data:
    data = json_data.read()
    d = json.loads(data)
    print(d)
    # print(d['firstName'])
