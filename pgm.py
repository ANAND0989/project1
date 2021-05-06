import os
def fun(path):
    f = open(path, 'r')
    print(path)
    fo = open("../output/"+path,'w')
    table = []
    for line in f:
        table.append(line.split())
    table = table[4:]
    for row in table:
        for column in row:
            fo.write(column+"\n")
        
path = 'input'
os.chdir(path)

dirs = os.listdir()
dirs.sort()
o = open("../output.txt","w")
for file in dirs:
    tmp = fun(file)
print("Program executed successfully")
