#jeep
route=["SM","BAYAN","RED-V"]
passenger=[]
seats=6
fare=13
total=0
while True:
    print()
    print(len(passenger),"of",seats,"seats")
    print("1 Sakay 2 Priority seat 3 Para po!")
    print("4 Baba sa pinto 7 balikan 8 Exit")
    choice=input("choice: ")

    if choice == "1":
        if len(passenger)== seats:
            print("Puno na!")
        else:
            name= input("name: ")
            passenger.append(name)
            total=total + fare
            print(name,"boarded at the back.")

    elif choice == "2":
        if len(passenger)== seats:
            print("Puno na!")
        else:
            name=input("name; ")
            passenger.insert(0,name)
            total=total + fare
            print(name,"took the priority sea")

    elif choice == "3":
        name = input("Who is getting off? ")
        if name in passenger: 
            passenger.remove(name)
            print(name,"got off. Ingat!")
        else:
            print(name,"is not on this jeep")

    elif choice == "4":
        if len(passenger) == 0 :
            print("The jeep is empty")
        else: 
            left= passenger.pop()
            print(left,"got off at the door.")

    elif choice == "5":
        if len(passenger) == 0:
            print("The jeep is empty")
        else:
            front= passenger.pop()
            print(front,"got off at the front")
    elif choice == "6":
        for i in range(len(passenger)):
            print("Seat", i + 1, passenger[i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice == "8":
        print("Total fare today:", total)
        break

    else:
        print("Invalid choice.")