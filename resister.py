import turtle    
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
def pen(a,b,c,d):
    

    t = turtle.Turtle()


    t.speed(10)
    

    t.color('black')
    t.pensize(3)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.forward(180)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(50)


    t.penup()
    t.goto(-70, 0)
    t.pendown()
    t.color(a)
    t.begin_fill()

    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.end_fill()


    t.penup()
    t.goto(-40,0)
    t.pendown()
    t.color(b)
    t.begin_fill()
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()

    t.penup()
    t.goto(-10,0)
    t.pendown()
    t.color(c)
    t.begin_fill()
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()


    t.penup()
    t.goto(20,0)
    t.pendown()
    t.color(d)
    t.begin_fill()
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.end_fill()

    t.penup()
    t.color('black')
    t.goto(-100, 0)
    t.pendown()
    t.right(180)
    t.forward(180)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(50)

    t.penup()
    t.goto(-100,-25)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.penup()

    t.goto(80,-25)
    t.right(180)
    t.pendown()
    t.forward(50)
    







        
    t.end_fill()
    t.hideturtle()



    turtle.done()

    return()
p=0
while p==0:
    print('1. Colour to Resistance\n2.Resistance to Colour')
    op=int(input("Enter the operation:"))
    if op==1:
        f=col_res()
        pen(f[0],f[1],f[2],f[3])
        

    elif op==2:
        f=res_col()
        pen(f[0],f[1],f[2],f[3])
        

    else:
        p=1