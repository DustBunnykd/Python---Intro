#Your trainer just asked you to multiply 3 numbers together the numbers are 21 31, and 51

#whatever you get print it out

#introduce an if condition, check if your result is less than 2000

#if yes print "Hurray it is less than 2000"

#then immediately multiply the initial result by 5 and print the final output

#else, in case it is not less than 2000 add 500 to it
a= 21
b=31
c=51
d=a+b+c
e=d*3
print(e)
if e<2000:
    print("Hurray it is less than 2000")
    f=e*5
    print ("This is the final answer if less than 2000",f)
else:
    f=e+500
    print("Ohh! it is greater than 2000",f)