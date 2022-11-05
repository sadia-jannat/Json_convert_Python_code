import json

myjsonfile=open('sampleJson/pos_10492.png.json', 'r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)
print(str(obj['description']))

list=obj['tags']
print(list)
lenlist=len(list)
if(lenlist>0):
    for le in range(lenlist):
        print(list[le])
        print("Yes,there are array data.")
else:
    print("No array data here")

print(dict(obj['size']))

list2=obj['objects']
print(list2)
lenlist2=len(list2)
if(lenlist2>0):
    for l in range(lenlist2):
        print(list2[l])
        print("Yes,there are array data.")
else:
    print("No array data here")


