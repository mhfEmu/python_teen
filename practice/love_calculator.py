# This console tests the compatibility between two people.
# I'm going to use the super scientific method recommended by BuzzFeed.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowerCase_name1 = name1.lower()
lowerCase_name2 = name2.lower()

name1TrueCount_t = lowerCase_name1.count("t")
name1TrueCount_r = lowerCase_name1.count("r")
name1TrueCount_u = lowerCase_name1.count("u")
name1TrueCount_e = lowerCase_name1.count("e")

name2TrueCount_t = lowerCase_name2.count("t")
name2TrueCount_r = lowerCase_name2.count("r")
name2TrueCount_u = lowerCase_name2.count("u")
name2TrueCount_e = lowerCase_name2.count("e")

name1_name2_TrueCount = int((name1TrueCount_t + name1TrueCount_r +
                             name1TrueCount_u + name1TrueCount_e) +
                            (name2TrueCount_t + name2TrueCount_r +
                             name2TrueCount_u + name2TrueCount_e))

name1LoveCount_l = lowerCase_name1.count("l")
name1LoveCount_o = lowerCase_name1.count("o")
name1LoveCount_v = lowerCase_name1.count("v")
name1LoveCount_e = lowerCase_name1.count("e")

name2LoveCount_l = lowerCase_name2.count("l")
name2LoveCount_o = lowerCase_name2.count("o")
name2LoveCount_v = lowerCase_name2.count("v")
name2LoveCount_e = lowerCase_name2.count("e")

name1_name2_LoveCount = (
    (name1LoveCount_l + name1LoveCount_o + name1LoveCount_v + name1LoveCount_e)
    + (name2LoveCount_l + name2LoveCount_o + name2LoveCount_v +
       name2LoveCount_e))

numericData = int(str(name1_name2_TrueCount) + str(name1_name2_LoveCount))

if numericData < 10 or numericData > 90:
    print(f"Your score is {numericData}, you go together like coke and mentos.")
elif numericData > 40 and numericData < 50:
    print(f"Your score is {numericData}, you are alright together.")
else:
    print(f"Your score is {numericData}.")