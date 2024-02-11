def col_res():

    sum=[]
    list=[]

    m1=input("Enter the 1st line:")
    m2=input("Enter the 2nd line:")
    m3=input("Enter the 3rd line:")
    t=input("Enter the 4th line:")

    list.append(m1)
    list.append(m2)
    list.append(m3)
    list.append(t)

    if m1=='black':
        sum.append(0)

    elif m1=='brown':
        sum.append(1)

    elif m1=='red':
        sum.append(2)

    elif m1=='orange':
        sum.append(3)

    elif m1=='yellow':
        sum.append(4)

    elif m1=='green':
        sum.append(5)

    elif m1=='blue':
        sum.append(6)

    elif m1=='violet':
        sum.append(7)

    elif m1=='grey':
        sum.append(8)

    elif m1=='white':
        sum.append(9)



    if m2=='black':
        sum.append(1)

    elif m2=='brown':
        sum.append(1)

    elif m2=='red':
        sum.append(2)

    elif m2=='orange':
        sum.append(3)

    elif m2=='yellow':
        sum.append(4)

    elif m2=='green':
        sum.append(5)

    elif m2=='blue':
        sum.append(6)

    elif m2=='violet':
        sum.append(7)

    elif m2=='grey':
        sum.append(8)

    elif m2=='white':
        sum.append(9)

    else:
        sum.append(1)

    mm=m3

    if mm=='black':
        sum.append(1)

    elif mm=='brown':
        sum.append(10)

    elif mm=='red':
        sum.append(100)

    elif mm=='orange':
        sum.append(1000)

    elif mm=='yellow':
        sum.append(10000)

    elif mm=='green':
        sum.append(100000)

    elif mm=='blue':
        sum.append(1000000)

    elif mm=='violet':
        sum.append(1)

    elif mm=='grey':
        sum.append(1)

    elif mm=='white':
        sum.append(1)

    else:
        sum.append(1)


    if t=='silver':
        sum.append(0.1)

    elif t=='gold':
        sum.append(0.05)

    else:
        sum.append(1)


    f1=str(sum[0])
    f2=str(sum[1])
    fi=f1+f2

    fin=int(fi)

    mul=sum[2]
    tot=fin*mul

    print(tot,'+',sum[3],'%')

    return(list)