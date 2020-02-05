import random
a = random.choice([1,2,3,4,5])
b = int(input("Choose blessfull number 1/2/3/4/5\n"))

if  a == b:
    print("You win!")
    print("{} is the blessfull number".format(a))
else:
    print("You Lose!")
    print("{} is the blessfull number".format(a))

