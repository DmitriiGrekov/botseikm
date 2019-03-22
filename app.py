import csv
f = open('text.txt')
keys={}
for line in f:
    arr=line.split("$$")
    keys[arr[0]]=arr[-1]



import pickle

with open('out.txt','wb') as out:
    pickle.dump(keys,out)
 
 
with open('out.txt','rb') as inp:
    d_in = pickle.load(inp)
print(d_in)
