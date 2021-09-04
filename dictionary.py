dict_a = {
    "name" : "KMS",
    "age" : 21,
    "live" : "Osan",
    "job" : "student",
    "sex" : "male"
}

print(dict_a["job"])

dict_a["weight"] = 80
print(dict_a)

del dict_a["live"]
print(dict_a)

value = dict_a.get("no")
print("value:", value)
if value==None:
    print("You try accessing no exist key value")

for i in dict_a:
    print(dict_a.get(i))

print(type({}),"is dict")