no = 20
if no >0:
    print("The number is positive")
else:
    print("The number is negative")

no = 0
if no>0:
    print("The number is positive")
elif no < 0:
    print("The number is negative")
else:
    print("The number is zero")

S=85
if S>=90:
    grade='A'
elif S>=80:
    grade='B'
elif S>=70:
    grade='C'
elif S>=60:
    grade='D'
else:
    grade='F'
print(f'Your grade is: {grade}')

num=7
result = "even" if num % 2 == 0 else "odd"
print(f"The number is {result}")

num1 = 10
num2 = 5
ope= "+"

if ope=="+":
    result =num1+num2
elif ope== "-":
    result = num1-num2
elif ope=="*":
    result = num1*num2
elif ope=="/":
    result = num1/num2 if num2!= 0 else "Error: Division by zero"
else:
    result= "Error: Invalid operator"
print(f"Result: {result}")