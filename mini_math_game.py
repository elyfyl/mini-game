answer = "e"
while answer =="e":
    import random
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    operation = "+"
    result = num1 + num2

    answer = int(input("{}{}{}=? What is the result of the operation?".format(num1, operation, num2)))
    if answer == result:
        print("Congratulations!")
    else:
        print("Failure.")
        
    var =input("Do you want to play again? [y]es / [n]o:")
    if var == "n":
        print("Game is over.")
    else:
        answer = "e"
        continue 