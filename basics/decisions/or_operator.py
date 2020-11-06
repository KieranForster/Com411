print("what type of adventure should i have?")
decision_1 = str(input())
if decision_1 == "scary" or "short":
  print("Entering the dark forest.")
elif decision_1 == "safe" or "long":
  print("Tanking the safer route!")
else:
  print("Not sure which route to take.")