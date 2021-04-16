# automatic pizza order program

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y" and extra_cheese == "Y":
        print(f"Your final bill is: {bill+2+1}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        print(f"Your final bill is: {bill+2}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        print(f"Your final bill is: {bill+1}.")
    else:
        print(f"Your final bill is: {bill}.")

elif size == "M":
    bill = 20
    if add_pepperoni == "Y" and extra_cheese == "Y":
        print(f"Your final bill is: {bill+3+1}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        print(f"Your final bill is: {bill+3}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        print(f"Your final bill is: {bill+1}.")
    else:
        print(f"Your final bill is: {bill}.")

else:
    bill = 25
    if add_pepperoni == "Y" and extra_cheese == "Y":
        print(f"Your final bill is: {bill+3+1}.")
    elif add_pepperoni == "Y" and extra_cheese == "N":
        print(f"Your final bill is: {bill+3}.")
    elif add_pepperoni == "N" and extra_cheese == "Y":
        print(f"Your final bill is: {bill+1}.")
    else:
        print(f"Your final bill is: {bill}.")