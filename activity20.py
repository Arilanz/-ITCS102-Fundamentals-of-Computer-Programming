basketball_player = []
con = True

while con == True:
    ask = input("Do you know any basketball player (yes/no): ").lower()

    if ask == "yes":
        who = input("Who is it ----------------> ")
        basketball_player.append(who)
        ask = input("Do you know more (yes/no): ").lower()
        if ask == "yes":
            print("Name more")
            continue
        else:
            con = False
    else:
        con = False

print(basketball_player)