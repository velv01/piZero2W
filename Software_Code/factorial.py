numbr = int(input("Enter a number: "))
factorial = 1

# check if the number is negative, zero, or positive
if numbr < 0:
   print("Negative numbers do not have factorials")
elif numbr == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, numbr + 1):
       factorial = factorial*i
   print("The factorial of",numbr,"is",factorial)

 




   


   
   




 



    

    
    

