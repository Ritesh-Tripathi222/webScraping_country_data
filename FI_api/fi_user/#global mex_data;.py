


# #dct = {'a':1,'b':2,'c':3,'d':4,'e':5}
# tuple1 = ('a','b','c','d','e')
# tuple2 = (1,2,3,4,5)
# d=dict()
	
# #for k ,v in tuple1,tuple2:

# d=dict(zip(tuple1,tuple2))
# print(d)

lst = [1,2,1,1,2,3,3,4,5,5,6]
l=[]
count=0
for i in lst:
    x=lst.count(lst[i])
    print(x)
    if x>1:
        continue
    else:
        if x==1:
            l.append(i)
print(l)

