l = [[1,2,3], [4,5,6]]
for a,b in zip(*l):
    print(str(a)+' '+str(b))