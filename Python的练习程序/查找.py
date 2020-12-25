m=input()
n=input()
c=0
index=n.find(m) #查找函数
a=index
index=int(0)
if a==-1 :
    print("Not Found")
else :
    #print("index=",index)
    for i in n :
        if i==m :
           #index=a
           index=index+c
           c=1
           #print(ind  ex)
        else :
         c=c+1
         #print("c:",c)
    print("index=%d"%index)