def counters(n:int,nn:int):
   nnn:int=n
   nreturn:int=0
   treturn=False
   nnn+=1
   if nnn>nn:

       return 1,True
   else:
       
       return nnn,False
   
def fformat(ff:float,separators:str)->str:
   pointers1=str(ff)

   pointers2=pointers1.split(".")
   sreturn=""
   ssreturn=""
   s=pointers2[0].strip()
   
   l=len(s)
   i:int=0
   ti:int=0
   pos=0
   t:bool=True
   for i in range(l):
       ti,t=counters(ti,3)
       if t:
           sreturn=separators+sreturn
       pos=l-1-i
       sreturn=s[pos]+sreturn
   ssreturn=sreturn+"."
   sreturn=""
   s=""
   if len(pointers2)>1:
       s=pointers2[1].strip()  
   l=len(s)
   i:int=0
   ti:int=0
   pos=0
   t:bool=True
   for i in range(l):
       ti,t=counters(ti,3)
       if t:
           sreturn=sreturn+separators
       pos=i
       sreturn=sreturn+s[pos]
   
   ssreturn=ssreturn+sreturn
   return ssreturn    
    
    
print("\x1bc\x1b[41;37m")
print(fformat(123456.789012,"'"))

