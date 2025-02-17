file=open('cat.txt','r')
print(file.read())
file.close()

file_write=open('cat.txt','w')
file_write.write("Hi I am Raza \n")
file_write.close()

file_append=open('cat.txt','a')
file_append.write("have more than thousands of more specises demessticated ")
file_append.close()

file1=open('cat.txt')
file2=open('cat2.txt')

print(file1.read())
print("file 2 befor merginig" )


file1.close()
file2.close()


f1=open('cat.txt','r')
f2=open('cat2.txt','a')


f2.write(f1.read())

f1.seek(0)
f2.seek(0)

f1.close()
f2.close()