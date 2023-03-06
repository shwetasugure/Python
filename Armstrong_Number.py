x = int(input("Enter the number:"))
digits = len(str(x))
reminder = 0
temp = x
while temp != 0:
   a = temp % 10
   reminder += a**digits
   temp = temp//10
if(reminder == x):
   print(x, 'is a Armstrong number')
else:
   print(x, 'is not a armstrong number')


