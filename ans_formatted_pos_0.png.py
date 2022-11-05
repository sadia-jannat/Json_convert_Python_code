import json

myjsonfile=open('sampleJson/formatted_pos_0.png.json', 'r')
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

        print("annotation_attributes:",obj[ar].get("annotation_attributes"))
        json_formatt=json.dumps(obj[ar]['annotation_attributes'], indent=4)
        print(json_formatt)
        
        

else:
    print("No array data here")    