def bilPrima(s):
    for i in range(2,s+1):
        a = 0
        for j in range(1,i):
            if a > 1:
                break

            print(i,"/",j)
            
            if i%j == 0:
               a+=1
        if a == 1:
            print(i)

r = int(input("bilangan prima antara 2 sampai "))
bilPrima(r)
