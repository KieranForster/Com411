import random 
print("Please enter a minimum value:")
min_value = int(input())
print("Please enter a maximum value:")
max_value = int(input())
rand_output = (random.randrange(min_value, max_value,1))
print(f"I am thinking of a number between {min_value} and {max_value}.  Can you guess what it is?")
guess = 0
while (guess != rand_output):
 guess = int(input())
 if guess == rand_output:
   print("Congratulations! You guessed my number!")
 elif guess < rand_output:
   print("Your guess is too low.")
   print("Try again:")
 elif guess > rand_output:
   print("Your guess is too high.")
   print("Try again:")