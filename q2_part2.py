d = {0: 3,1: 8,2: 12,3: 15,4: 9,5: 3}
s=0
n=0
for key in d:
    s=s+d[key]
    if key>=3:
        n=n+d[key]
probabilty=n/s
print(probabilty)