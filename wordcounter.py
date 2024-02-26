def cwords(s:str,s1:str):
    ss=s+" "
    ss=ss.lower()
    s11=s1.lower()
    sss=ss.split(s11)
    return len(sss)-1
print("\x1bc\x1b[41;37m")
ccword="hello world,hello world,hello world,hello world,hello world,"
cccword="HELLO"
print(cwords(ccword,cccword))
