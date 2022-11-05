import json

myjsonfile=open('sampleJson/pos_0.png.json', 'r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)
print(str(obj['description']))

tagslist=obj['tags']
print(tagslist)
lenlist=len(tagslist)
if(lenlist>0):
    for l in range(lenlist):
        print(tagslist[l])
else:
    print("No array data here")

print(dict(obj['size']))

objectslist=obj['objects']
print(objectslist)
lenlist2=len(objectslist)
if(lenlist2>0):
    for l in range(lenlist2):
        print(objectslist[l])
        print("Id:",objectslist[l].get("id"))  
        print("classId:",objectslist[l].get("classId"))
        print("description:",objectslist[l].get("description"))
        print("geometryType:",objectslist[l].get("geometryType"))
        print("createdAt:",objectslist[l].get("createdAt"))
        print("updatedAt:",objectslist[l].get("updatedAt"))
        
        print("tags:",objectslist[l].get("tags"))
        
        tagslist2=len(objectslist[l]['tags'])
        for t in range(tagslist2):
            print("Id:",objectslist[l]['tags'][t].get("id"))
            print("tagId:",objectslist[l]['tags'][t].get("tagId"))
            print("name:",objectslist[l]['tags'][t].get("name"))
            print("value:",objectslist[l]['tags'][t].get("value"))
            print("labelerLogin:",objectslist[l]['tags'][t].get("labelerLogin"))
            print("createdAt:",objectslist[l]['tags'][t].get("createdAt"))
            print("updatedAt:",objectslist[l]['tags'][t].get("updatedAt"))
        
        #main work
        #print("classTitle:",objectslist[l].get("classTitle"))
        if(objectslist[l]['classTitle']=='Vehicle'):
            print("classTitle:car")
        elif(objectslist[l]['classTitle']=='License Plate'):
            print("classTitle:number")
        else:
            print("There is no classtitle name Vehicle or License Plate")    
        
        print("points:",objectslist[l].get("points")) 

        print(objectslist[l]['points'].get("exterior"))
        lenlist3=len(objectslist[l]['points']['exterior'])
        if(lenlist3>0):
            for ex in range(lenlist3):
             print("Yes, there are data.")

        else:
            print("No array data here") 

        print(objectslist[l]['points'].get("interior"))
        lenlist4=len(objectslist[l]['points']['interior'])
        if(lenlist4>0):
            for inter in range(lenlist4):
                print("Yes, there are data.")
        else:
            print("No array data here")
        
else:
    print("No array data here")


