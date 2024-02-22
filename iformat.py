def counters(n:int,nn:int):
   nnn:int=n
   nreturn:int=0
   treturn=False
   nnn+=1
   if nnn>nn:

       return 1,True
   else:
       
       return nnn,False
   
def iformat(ii:int,separators:str)->str:
   sreturn=""
   s=str(ii)
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
   return sreturn    
    
    
print("\x1bc\x1b[41;37m")
print(iformat(123456789012,"'"))

