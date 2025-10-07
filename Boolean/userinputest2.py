#print first number
print("enter first number")
firstnumber=float(input())
print("enter second number")
secondnumber=float(input())
print("enter third number")
thirdnumber=float(input())
total=firstnumber+secondnumber+thirdnumber
print("total result ",total)
if total>2000:
    print("yes it is grearter than 2000") # type: ignore
    a=total*50
    print("this is the final result",a)
else:
    print("no it is less than 2000")
    b=total*3
    print("this is the final result",b)