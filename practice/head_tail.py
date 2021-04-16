# It will randomly tell the user "Heads" or "Tails".
# 1 means Heads & 0 means Tails
import random

toss = random.randint(1, 2)

if toss == 1:
  print("Heads")
else:
  print("Tails")