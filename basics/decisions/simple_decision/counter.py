print("Please enter the first whole number.")
decision_1 = int(input())
print("Please enter the second whole number.")
decision_2 = int(input())
print("Please enter the third whole number.")
decision_3 = int(input())
even_numbers = 0
odd_numbers = 0
if decision_1 % 2 == 0:
 even_numbers+=1
else:
  odd_numbers+=1
if decision_2 % 2 == 0:
 even_numbers+=1
else:
  odd_numbers+=1
if decision_3 % 2 == 0:
  even_numbers+=1
else:
  odd_numbers+=1
print(f"There were {even_numbers} even and {odd_numbers} odd.")