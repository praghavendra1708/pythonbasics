from __future__ import print_function


myDict = {'name':'xyz', 'id':123, 'addr':'Unknown'}

print(myDict)


myNestedDict = {'name':'xyz', 'id':123, 'addr': {'road no': 3, 'stree':'Vauge Stree', 'pincode':12345}}

print('New pin code of xyz is', myNestedDict['addr']['pincode'])


myNestedDict.get()