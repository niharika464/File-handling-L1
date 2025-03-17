file=open('sample.txt', 'r') #read
print(file.read())
file.close()


filew=open('sample.txt','w') #write
filew.write("Hello! how have u been nowadays \n Doing good..")
filew.close()


filea=open('sample.txt', 'a') #append
filea.write("\n I am using the aapend function...\n i am gonna read it now")
filea.close()

filea=open('sample.txt', 'r') #read
print(filea.read())
filea.close()