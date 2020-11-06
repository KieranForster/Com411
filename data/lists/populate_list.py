def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
def menu():
  print("Please select a direction:")
  move = directions()
  for count in range(len(move)):
    print(f"{count}: {move[count]}")
  response = int(input())
  return move[response]
def run():
  route = []
  print("working out an escape route...")
  for count in range(5):
    menu_choice = menu()
    route.append(menu_choice)
  print(f"Escape route: {route}")
run()