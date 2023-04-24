import ruamel.yaml as yaml
import json

if __name__== "__main__":
    print('Làm việc với file yaml')
    with open ("user.yaml", "r") as file :
        user_yaml= yaml.safe_load(file)
   
    print("Print Type of user_yaml")
    print(type(user_yaml))
    print("------------------")
    for key in user_yaml:
        print(key)

    print("------------------")
    print("print value of key 'id'")
    print(user_yaml["id"])

    print("------------------")
    print("print value of key fist_name")
    print(user_yaml["first_name"])

    print("------------------")
    print("print value of key address")
    print(user_yaml["address"])
    adr=user_yaml["address"][1]
    print("print city")
    print(adr['city'])
    print("key city")
    print(user_yaml["address"][1]['city'])
    print("------------------")
    for i in range(0,len(user_yaml["address"])):
        print(user_yaml["address"][i]['city'])
    #{key:{key1:value1},}
    print("------------------")
    user_json= json.dumps(user_yaml,default=str,indent=4)
    print("Structure JSON")
    print(user_json)
    file=open("user.json","w")
    file.write(user_json)
    file.close()
