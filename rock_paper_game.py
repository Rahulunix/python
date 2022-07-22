import random
def rock_game(comp,you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return True

    elif comp == "p":
        if you == "s":
            return True
        elif you == "r":
            return False

    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True

print("computer turn : rock(r),paper(p),scissor(s) ?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "r"
elif randNo == 3:
    comp = "p"

you = input("your turn : rock(r),paper(p),scissor(s): ")
a = rock_game(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("game is tie")
elif a :
    print("you win")
else:
    print("you lose")
