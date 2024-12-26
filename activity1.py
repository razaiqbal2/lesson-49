file=open('lion.txt','r')
print(file.read())
file.close()

file_write=open('lion.txt','w')
file_write.write("Hi I am Raza \n")
file_write.close()

file_append=open('lion.txt','a')
file_append.write("Lion are predetors")
file_append.close()