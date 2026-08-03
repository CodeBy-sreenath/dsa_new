details={
    "name":"sreenath",
    "age":21,
    "profession":"student"
}
print(details)
print(details["name"])
print(details.get('age'))
for item in details.values():
    print(item)
for item in details.keys():
    print(item)
for item in details.items():
    print(item)
print(details.pop('name')) 
print(details)  
del details["age"]
print(details)         