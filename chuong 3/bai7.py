f=open("e:\\ma tran.txt","r")
ma=[]
ma=[dong.split()for dong in f]
print(ma)
s=0
for subma in ma:
    for j in subma:
        s=s+float(j)
        print("tong cua ma tran la:",s)