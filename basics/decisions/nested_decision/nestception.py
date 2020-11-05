print("Where should i look?")
decision_1 = str(input())
if decision_1 == "bedroom":
  print("where in the bedroom should i look?")
  decision_bedroom = str(input())
  if decision_bedroom == "cupboard":
   print("found some mess but no battery.")
elif decision_1 == "bathroom":
  print("where in the bathroom should i look?")
  decision_bathroom = str(input())
  if decision_bathroom == "bathtub":
   print("found a rubber duck but no battery.")
elif decision_1 == "lab":
  print("where in the lab should i look?")
  decision_lab = str(input())
  if decision_lab == "table":
   print("Yes! I found my battery!")
else:
  print("I do not know where that is but i will keep looking.")