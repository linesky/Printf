def counters(n:int,nn:int):
   nnn:int=n
   nreturn:int=0
   treturn=False
   nnn+=1
   if nnn>nn:

       return 1,True
   else:
       
       return nnn,False
def charcodes(*varss):
    svars=list(*varss)
    
    sreturn:str=""
    vars:list=[]
    for n in svars:
        vars=vars+[str(n)]
    
  
    lens=len(vars)
    
    
    
    i:int=0
    if lens==0:
        ii=0

    if 0==0:
       
        spl=vars[0].split("[")
        
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                sreturn=sreturn+str(ss)
           
            else:
                if 0==0:
                    kkk=ss.split("]")
                    
                    llll=chr(int(kkk[0]))
                    
                    if len(kkk)>1:
                        sreturn=sreturn+str(llll)+str(kkk[1])
                   
 
           
    return sreturn


def printcharcodes(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(charcodes(vars),end="")        
         
print("\x1bc\x1b[41;37m")
i:int=1;
ii:bool=False
for nn in range(32,128):
    
    printcharcodes("["+str(nn)+"] ")
    
    i,ii=counters(i,8)
    if ii:
        print()
