#here num1 and num2 are varibles to store the value 
num1 = int(input("Enter Number1 :-"))
num2 = int(input("Enter Number2:-"))
num = int(input("Enter Number:-"))
fc=0
for i in range(2,num):
    if num%i==0:
        fc+=1
#here fc is zero then number is prime otherwise not prime
if fc==0:
    print(num,"is  Prime Number")
else:
    print(num,"is not Prime Number")
#here displaying the num1 and num2 with the help of print statement
print("Num1:",num1)
print("Num2:",num2)
print("Num1 is equal to Num2:",num1==num2)

add = num1+num2
sub = num1-num2
mul = num1*num2
#here typecasting is done as answer will be in float so 
div = int(num1/num2)
rem = num1%num2

print("Addition = ",add)
print("Subtraction = ",sub)
print("Multiplication = ",mul)
print("Division = ",div)
print("Remainder = ",rem)
