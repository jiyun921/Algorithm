selfnum = []
for i in range(1,10000):
    selfnum.append(i)

for i in range(1,100000):
    dn = i + sum(map(int,str(i)))
    if dn in selfnum : 
        selfnum.remove(dn)

for i in selfnum: 
    print(i)