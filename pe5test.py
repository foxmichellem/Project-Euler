for y in range(2,20):
    list=[]
    i=2
    x=y
    while i*i <= x:
        while x%i == 0:
            #set some sort of varialbe that identifies which number you are on
            #if an integer is already on a list, count number of times and only add as necessary=
            list.append(i)
            x = x / i
        i = i + 1
    if len(list)==0:
        list.append(x)
    print (list)
    y=y+1
    
