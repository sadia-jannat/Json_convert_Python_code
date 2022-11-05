import json

myjsonfile=open('sampleJson/formatted_pos_10492.png.json', 'r')
jsondata=myjsonfile.read()

obj=json.loads(jsondata)

arrayobjlist=len(obj)
if(arrayobjlist>0):
    for ar in range(arrayobjlist):
        
        print("dataset_name:",obj[ar].get("dataset_name"))
        print("image_link:",obj[ar].get("image_link"))
        print("annotation_type:",obj[ar].get("annotation_type"))

        print("annotation_objects:",obj[ar].get("annotation_objects"))
        #print(dict(obj[ar]['annotation_objects']))
        json_format=json.dumps(obj[ar]['annotation_objects'], indent=4)
        print(json_format)
        
        #main work
        json_formatdata=obj[ar]['annotation_objects']
        for a in json_formatdata:
            if(a['presence']==0):
                print("presence data is 0 value")


        print("annotation_attributes:",obj[ar].get("annotation_attributes"))
        json_formatt=json.dumps(obj[ar]['annotation_attributes'], indent=4)
        print(json_formatt)

        #main work
        json_formatdataa=obj[ar]['annotation_attributes']
        for b in json_formatdataa:
            if(b['Type']=='null'):
                print("Type data is None")
            elif(b['Pose']=='null'):
                print("Pose data is None")
            elif(b['Model']=='null'):
                print("Model data is None")
            elif(b['Make']=='null'):
                print("Make data is None")
            elif(b['Color']=='null'):
                print("Color data is None")
            elif(b['Difficulty Score']=='null'):
                print("Difficulty Score data is None")
            elif(b['Value']=='null'):
                print("Value data is None")
            elif(b['Occlusion']=='null'):
                print("Occlusion data is None")                        


else:
    print("No array data here")    