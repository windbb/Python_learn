import json

#with open not nedd close
with open("config.json",mode='r',encoding='utf-8') as jfile:
    data=json.load(jfile)

    #json_array = json.load(jfile)

#mutli
for item in data:
    print("Nameaaa",item["name"])
    print("sub dataaa :",item["sub_content"]["fid"])

#Single 
#print (data)
#print ("Name",data["name"])
#print("sub data :",data["sub_content"])

#data["name"]= "modify name"

#with open("config.json",mode='w',encoding='utf-8') as jfile:
  #  json.dump(data,jfile) #update name
  


