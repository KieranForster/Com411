def directions():
  move = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return move
def menu():
  print("Please select a direction:")
  move = directions()
  for count in range(len(move)):
    print(f"{count}: {move[count]}")
def run():
  menu()
run()
