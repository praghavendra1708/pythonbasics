#This is an example to read and write json in python


import json
myfile = open("./SampleJsonInput.json", )
inputJson = json.load(myfile)
myfile.close()

print("Inputjson:", inputJson)
print(type(inputJson))


myString = """ 
{
"name":"Unknown",
"type":null,
"isValid": false
}
"""

myStrJson = json.loads(myString)
print("String json:", myStrJson)


strJson = json.dumps(inputJson, ensure_ascii=False)
print('Json string is:', strJson)

print("type of strJson is:", type(strJson))

outputFile = './outputjsonfile.json'
outiofile = open(outputFile, mode='w')
json.dump(inputJson, outiofile, ensure_ascii=False)
outiofile.close()