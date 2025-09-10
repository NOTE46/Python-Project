print ("HELLO USER THIS YOUR PERSONAL MATH AI ASSISTANT \n")
print ("DISCLAIMER: This is a bot so please recheck\n")

#input

task=input("Enter task:")

if task not in ['Addition','Subtraction','Multiplication','Division']:
 print ("PLEASE ENTER CORRECT TASK \n EXAMPLE:Addition,Subtraction,Multiplication,Division")

else:
  print(f"Your choice is {task}")


if task == 'Addition':
 a=float(input("Enter number 1:"))
 b=float(input("Enter number 2:"))
 print (f"The addition of {a} and {b} is {a + b}:")

elif task == 'Subtraction':
 ab=float(input("Enter number 1:\n"))
 ba=float(input("Enter number 2:\n"))
 print (f"The subtraction of {ab} and {ba} is {ab - ba}:")

elif task == 'Multiplication':
 abc=float(input("Enter number 1:\n"))
 bac=float(input("Enter number 2:\n"))
 print (f"The multiplication of {abc} and {bac} is {abc * bac}:")

elif task == 'Division':
 c=float(input("Enter number 1:\n"))
 ac=float(input("Enter number 2:\n"))
 print (f"The division of {c} and {ac} is {c / ac}:")

else:
 print("ERROR TRY AGAIN")