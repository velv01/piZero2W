import random

def addition():
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)
    print(n1, "+", n2, "= ")
    user_answer = int(input("Enter answer: "))
    correct_answer = n1 + n2
    return (user_answer, correct_answer)

def subtraction():
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)
    print(n1, "-", n2, "= ")
    user_answer = int(input("Enter answer: "))
    correct_answer = n1 - n2
    return (user_answer, correct_answer)

def multiplication():
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)
    print(n1, "X", n2, "= ")
    user_answer = int(input("Enter answer: "))
    correct_answer = n1 * n2
    return (user_answer, correct_answer)

def division():
    n1 = random.randint(1, 1000)
    n2 = random.randint(1, 1000)
    print(n1, "/", n2, "= ")
    user_answer = int(input("Enter answer: "))
    correct_answer = int(n1 / n2)
    return (user_answer, correct_answer)

def chk(user, correct):
    if user ==correct:
        print("CORRECT")
    else:
        print("INCORRECT")
        
print("   1. Addition")
print("   2. Subtraction")
print("   3. Multiplication")
print("   4. Integer Division")
ch = int(input("Choice: "))
if ch == 1:
    user,correct = addition()
elif ch == 2:
    user,correct = subtraction()
elif ch == 3:
    user,correct = multiplication()
else:
    user,correct = division()
chk(user,correct)




