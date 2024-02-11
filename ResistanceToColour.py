def res_col():
    val=int(input("Enter the resistance value in whole number:"))
    tel=float(input("Enter the value of tolerance in decimals:"))

    colour=[]
    st=str(val)
    div=st[0]+st[1]
    div=int(div)
    mult=val/div
    cl=['black','brown', 'red','orange','yellow','green','blue','violet','grey','white']
    d11=[0,1,2,3,4,5,6,7,8,9]
    d12=d11
    mul=[1,10,100,1000,10000,100000,1000000,1,1,1]
    div=str(div)
    d1=div[0]
    d2=div[1]
    d1=int(d1)
    d2=int(d2)
    if d1 in d11:
        in1=d11.index(d1)
        digit1=cl[in1]
        colour.append(digit1)

    else:
        print("Check your input value...")


    if d2 in d11:
        in2=d11.index(d2)
        digit2=cl[in2]
        colour.append(digit2)

    else:
        print("Check your input value...")


    if mult in mul:
        in3=mul.index(mult)
        digit3=cl[in3]
        colour.append(digit3)

    else:
        print("Check your input value...")



    if tel==0.1:
        colour.append('silver')

    elif tel==0.05:
        colour.append('gold')

    else:
        print()


    for i in colour:
        print(i)

    
    return colour