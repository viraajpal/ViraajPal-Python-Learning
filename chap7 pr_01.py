num = int(input("Enter the number: "))
for i in range(1, 11):
   print(str(num) + " * " + str(i) + "=" +str(i*num))
   print(f"{num}*{i}={num*i}") # this is the use of f string.