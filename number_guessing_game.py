import random
print("I'm thinking of a number between 1 and 10.")
guess = input("Guess the number.")
number = random.randint(1, 11)
if guess == number:
  print(f"That's right! My secret number was {number}.")
else:
  print(f"Actually, I was thinking of {number}.")
