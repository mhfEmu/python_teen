# Complete Rollar Coaster in Console
Height = int(input("What's your Height in CM? "))
bill = 0

if Height >= 120:
    print("You can ride the RollarCoaster!")
    age = int(input("What's your age in Years? "))
    if age <= 12:
        bill = 6

    elif age <= 18:
        bill = 10

    elif age < 40:
        bill = 12
    else:
        bill = 13

    if age > 45 and age < 55:
        print(f"You're getting a free ride!")
    else:
        photo = input("You want photo while riding? Y/n \n")
        if photo == "Y":
            print(f"Total ticket price is ${bill+3}.")
        else:
            print(f"Your ticket price is ${bill}.")

else:
    print("Can't ride")