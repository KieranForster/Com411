print("Please enter a sequence")
response = input()
print("Please enter the character for the marker")
marker = input()
position_1 = -1
position_2 = -1
for position in range(0, len(response), 1):
  letter = response[position]
  if(letter == marker):
    if(position_1 == -1):
      position_1 = position
    else:
      position_2 = position
print("The distance between the markers is", position_2 - position_1 -1)