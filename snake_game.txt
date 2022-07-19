import random
def snake_game(comp,you):
     if comp == you:
        return None
     elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
     elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
     elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
print("computer turn:Snake(s),Water(w),Gun(g)? ")
randNo = random.randint(1, 3)
if randNo == 1:
   comp = "s"
elif randNo == 2:
   comp = "w"
elif randNo == 3:
   comp =  "g"

you = input("Your turn: Snake(s),Water(w),Gun(g): ")
a = snake_game(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")
if a == None:
    print("game is tie!")
elif a :
    print("you win!")
else:
    print("you lose!")
