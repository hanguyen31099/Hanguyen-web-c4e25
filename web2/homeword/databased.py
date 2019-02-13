import sys
from River import River
sys.path.append(r'D:\Desktop\techkid\web Module\web2')
import mlap
mlap.connect()
f_objects=River.objects()
dict_river={}
length_river=[]
name_river=[]
print("name and length of river in Africa:")
for f in f_objects:
    if(f.continent=='Africa'):
        name_river.append(f.name)
        length_river.append(f.length)
dict_river=dict(zip(name_river,length_river))
for name,length in dict_river.items():
    print(name,length,sep=" ")
print("name of river in S. America have length less than 1000km:")
for f in f_objects:
    if(f.continent=='S. America'):
        if(f.length<=1000):
            print(f.name,end=',')