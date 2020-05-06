try:
    file = open("data.txt", "r")
except:
    print("Cannot open file\n")
    exit()


def Read_int(filename):
    f=0
    z=0
    x='0'
    while (x!=' ') and (x!=''):
        x=filename.read(1)
        if (x==' ' or x=='') and (f!=0):
            return z
        if (x=='') and (f==0):
            return 'end'        
        elif (x!=' '):
            try:
                x=int(x)
                z=z*10+x
                if (f==0):
                    f+=1            
            except:
                if (x!=' ') and (x!=''):
                    print("Wrong data\n")
                    exit()
 

c=None
while (c==None):        
    c=Read_int(file)
    if (c=='end'):
        print("Empty file\n")
        exit()
    
e=None
while (e==None):        
    e=Read_int(file)
    if (e=='end'):
        print("There is no increasing sections\n")
        exit()
     
f=1
max=1

if (e>c):
    f=2

c=None 
while(c!='end'):
    while (c==None):        
        c=Read_int(file)
        if (c!=None) and (c!='end'):
            if (c>e):
                f+=1
            elif (f>max):
                max=f
                f=1
            e=c           
        if (c!='end'):
            c=None

if (f>max):
    max=f

if (max==1):
    print("There is no increasing sections\n")
else:
    print("Maximum length of the increasing section is {}".format(max))   

file.close()