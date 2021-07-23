import json

with open('jsonread.json') as f:
   data = json.load(f)
   
content=data['content']
choice='y'
while choice=='y':
    txt=input("find ? ")
    if txt!='':
        start=content.find(txt)
        while start!=-1:
            end=start+len(txt)
            text=content[start:end]
            data={"start":start,"end":end-1,"text":text}
            print(data)
            start=content.find(txt,start+1)
        choice=input("Find More Press y:")

#print(content)
