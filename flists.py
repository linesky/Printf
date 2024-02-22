def flist(l1:list,l2:list)->str:
    l3:str=""
    i:int=0
    sss:str=""
    
    ii:int=len(l1)
    for a in range(ii):
        i=l2[a]
        sss=" "*l2[a]
        s=str(l1[a])+sss
        
        l3=l3+s[0:i]
        if a<ii-1:
            l3=l3+","
    return l3

def printflist(l1:list,l2:list):
    print(flist(l1,l2).replace(",","|"))

print("\x1bc\x1b[41;37m")
l1=["hello","hi","there","...."]
l2=[10,10,10,6]
for n in range(10):
    printflist(l1,l2)