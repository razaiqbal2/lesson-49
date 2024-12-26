file=open('whale.txt','r')
count=0
contant=file.read()


colist=contant.split("\n")
for i in colist:
    count+=1

print("Number of line in a file is" , count)
file.close()