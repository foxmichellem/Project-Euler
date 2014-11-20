i=1
x=999
y=999
stopval=1
while stopval==1:
    z=str(x*y)
    if z[0]==z[5] and z[1]==z[4] and z[2]==z[3]:
        stopval=2
    elif i%2==0:
        x=x-1
    elif i%2==1:
        y=y-1
    i=i+1
print (z)
