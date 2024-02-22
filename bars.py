def stringcodes(*varss):
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
       
        spl=vars[0].split("«")
        
        lens2=len(spl)
        for n in range(0,lens2):
            ss=spl[n]
            if n==0:
                sreturn=sreturn+str(ss)
           
            else:
                if 0==0:
                    kkk=ss.split("»")
                    
                    
                    
                    if len(kkk)>1:
                        
                        jjj=kkk[0].split(";")
                        
                        if len(jjj)>1:
                            l1:str=jjj[0]
                            l2:int=int(jjj[1])
                            llll:str=l2*l1
                            sreturn=sreturn+str(llll)+str(kkk[1])
                   
 
           
    return sreturn


def printstringcodes(*varss):
    vars:list=[]
    for n in varss:
        vars=vars+[str(n)]
        
    print(stringcodes(vars))        
         
print("\x1bc\x1b[41;37m")

for nn in range(10):
    ttt="«-;"+str(nn)+"»>"
    printstringcodes(ttt)
