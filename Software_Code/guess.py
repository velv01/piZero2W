import random
total_guesses = 0

number = random.randint(1, 50)
print ("The secret number is between 1 and 50. You have 5 attempts")

while total_guesses < 5:
    guess = int(input("Your guess: "))
    total_guesses = total_guesses + 1

    if guess < number:
        print ("Too low...")
    if guess > number:
        print ("Too high...")
    if guess == number:
        break

if guess == number:
    print ("You guessed in {0} attempts".format(total_guesses))
else:
    print ("Sorry... The secret number was {0}".format(number))




 




   


   
   




 



    

    
    

