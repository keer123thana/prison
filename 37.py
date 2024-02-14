prison1=[]
lucky=[]
unlucky=[]
count=100
prison1=["C"]*count
for i in range(0,count,1):
    prison1[i]="0"
for i in range(1,count,2):
    prison1[i]="C"

for j in range(2,count,1):
    
    for i in range(j,count,j+1):
        if(prison1[i]=="0"):
           prison1[i]="C"
        else:
           prison1[i]="0"

len1=len(prison1)
for i in range(0,len1,1):
    if prison1[i]=="0":
        lucky.append(i+1)
    else:
        unlucky.append(i+1)
print(lucky,"will release today")
print(unlucky,"will release after 4 weeks")
    
