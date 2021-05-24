import hashlib


import csv

def hash_password_hack(input_file_name, output_file_name):

    
    with open (input_file_name ) as f:
        reader = csv.reader(f)
        b= {}
        for row in reader:
            b[row[0]] = row[1]
    
    lst = []
    for i in b.items():
        temp=[i[0],i[1]]
        lst.append(temp)

    a = {}
    for i in range(0,9999):
        m = hashlib.sha256(str(i).encode('utf-8')).hexdigest()
        a[m] = i
    lst1=[]
    for i in a.items():
        remp=[i[0],i[1]]
        lst1.append(remp)
    

    file = open(output_file_name ,'w') 
    with open(output_file_name , 'w') as f:
        writer = csv.writer(f , delimiter = ',' , quotechar='"' , quoting = csv.QUOTE_MINIMAL)
    for i in lst:
        for j in lst1:
            if i[1] == j[0]:
                #print(str(i[0])+","+str(j[1]))
                file.write(str(i[0])+","+str(j[1])+"\n")
            
#hash_password_hack('/home/sepehr/hak.csv', '/home/sepehr/nh.txt')




