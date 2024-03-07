import json
json_file = '{"name" : "vishal", "age" : 26, "clg" : "siet"}'
print(json_file)
print(type(json_file))

#converting json into dict

dict_file = json.loads(json_file)
print(dict_file)
print(type(dict_file))


#converting dict into json

file_json = json.dumps(dict_file)
print(file_json)
print(type(file_json))


print(dict_file['name'])

# json multipul file

# import json
# json_file = '{"name" : "vishal", "age" : 26, "clg" : "siet"}'
# print(json_file)
# print(type(json_file))

# #converting json into dict

# dict_file = json.loads(json_file)
# print(dict_file)
# print(type(dict_file))


# #converting dict into json

# file_json = json.dumps(dict_file)
# print(file_json)
# print(type(file_json))


# print(dict_file['name'])