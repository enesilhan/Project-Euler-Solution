n = int(input("Enter a value : "))
i = 0
while 1:
    i+=n*(n-1)
    nInput=0
    for j in range(2,n):
        if (i%j != 0):
            nInput=1

            break
    if(nInput==0):
        if(i==0):
            i=1
        print(i)
        break
