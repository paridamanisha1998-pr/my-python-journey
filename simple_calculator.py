num1=int(input('Enter your first number: '))
num2=int(input('Enter your second number: '))
opr=input('Enter the operation  you want to perform(+,-,*,/):')
if opr=='+':
    result=num1+num2
elif opr=='-':
    result=num1-num2
elif opr=='*':
    result=num1*num2
elif opr=='/':
    if num2!=0:
        result=num1/num2
    else:
        result='Not Divided By zero'
else:
    result='invalid operation'
print("Result:",result)    