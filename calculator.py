first= input("Enter First No.: ")
second=input("Enter Second No.: ")
select=input("1 for add\n2 for sub\n3 for multiply\n4 for divide\n5 for remainder")
if int(select)==1:
    sum=int(first)+int(second)
    print("Sum is: "+str(sum))
elif int(select)==2:
    sub=int(first)-int(second)
    print("Sub is: "+str(sub))
elif int(select)==3:
    mul=int(first)+int(second)
    print("mul is: "+str(mul))
if int(select)==4:
    div=int(first)/int(second)
    print("div is: "+str(div))
elif int(select)==5:
    rem=int(first)%int(second)
    print("rem is: "+str(rem))
else:
    print("wrong input....try again")
    first= input("Enter First No.: ")
    second=input("Enter Second No.: ")
    select=input("1 for add\n2 for sub\n3 for multiply\n4 for divide\n5 for remainder")
    if int(select)==1:
       sum=int(first)+int(second)
       print("Sum is: "+str(sum))
    elif int(select)==2:
        sub=int(first)-int(second)
        print("Sub is: "+str(sub))
    elif int(select)==3:
        mul=int(first)+int(second)
        print("mul is: "+str(mul))
    if int(select)==4:
        div=int(first)/int(second)
        print("div is: "+str(div))
    elif int(select)==5:
        rem=int(first)%int(second)
        print("rem is: "+str(rem))