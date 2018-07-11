import json

#Write a JSON file
filepath=input(" JSON file path with forward / :-")
fileref=open(filepath,'w')
#Prepare an array & non array dictionary & convert into a JSOn object to write in a JSON file
data={'TypeA':{'CarModel': 'Renault', 'price': 600, 'Country': 'France'},'TypeB':{'CarModel': 'Ford', 'price': 200, 'Country': 'USA'}}
#data=[{'CarModel': 'Renault', 'price': 600, 'Country': 'France'},{'CarModel': 'Ford', 'price': 200, 'Country': 'USA'}]
print(data)
fileref.write(json.dumps(data,indent=4))

quit()

#Read an Non-array from JSON file , access data by item key
filepath=input("nonarray JSON file path with forward / :-")
fileref=open(filepath)
data=json.load(fileref)     #OR data=json.loads(fileref.read())
print("Priniting Non Array JSON *************")
print (json.dumps(data,indent=4))
#If item keys are known then use *data["BMW"]* to access the value of that key
#If item key are not known , fetch each key in a for loop and then use that key to get value
for item in data:
    print(data[item])


#Read an array from JSON file , use for loop to read array items
filepath=input("array JSON file path with forward / :-")
fileref=open(filepath)
data=json.load(fileref)     #OR data=json.loads(fileref.read())
print("Priniting  Array JSON *************")
print (json.dumps(data,indent=4))
#Array elements are accessed automatically using for loop
for item in data:
    print(item)

#quit()

