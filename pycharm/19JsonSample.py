#This is an example to read and write json in python


import json
myfile = open("./SampleJsonInput.json", )
inputJson = json.load(myfile)
myfile.close()

print("Inputjson:", inputJson)
print(type(inputJson))


myString = """ 
{
"name":"Unknow",
"type":null,
"isValid": false
}
"""

myStrJson = json.loads(myString)
print("String json:", myStrJson)
