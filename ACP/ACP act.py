file=open('sample.txt', 'r') #read
print(file.read())
file.close()



filew=open('sample.txt', 'w') #write
filew.write("Hii buddy!! \n How are you?")
filew.close()


filea=open('sample.txt', 'a') #append
filea.write("\n I am doing good and embracing the journey of my life... ")
filea.close()

filea=open('sample.txt','r') #read
print(filea.read())
filea.close