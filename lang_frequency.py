fi=open("Текст.txt",'r');
dict_slov={}
s=fi.read().split()
print(s)
for sl in s:
    if not(sl[-1].isalpha()):
        sl=sl[:-1]
    sl=sl.lower()
    if sl not in dict_slov:
        dict_slov[sl]=-1
    else:
        dict_slov[sl]-=1
vivod=[]
for sl in dict_slov.keys():
    vivod.append((-dict_slov[sl],sl))
index=1
for elem in sorted(vivod):
    if index==11: break
    print(index,')',' ',elem[1],sep='')
    index+=1

