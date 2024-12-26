file1=open('lion.txt')
file2=open('whale.txt')

print(file1.read())
print("file 2 befor merginig" )
print(file2.read())

file1.close()
file2.close()


f1=open('lion.txt','r')
f2=open('whale.txt','a')


f2.write(f1.read())

f1.seek(0)
f2.seek(0)

f1.close()
f2.close()