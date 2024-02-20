def printfs(*vars):
    lens=len(vars)
    
    i:int=0
    if lens==0:
        i=0
    if lens==1:
        print(vars[0])
    else:
        spl=vars[0].split("%")
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                print(ss,end="")
            else:
                if len(ss)>1:
                    
                    print(ss[1:],end="")
            if n<lens-1:
                ss=vars[n-1]
                print(ss)
         
print("xxxx")
printfs("\x1bc\x1b[41;37mhello world %s  \n",10)
