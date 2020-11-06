print("How far are we from the cave?")
response = int(input())
for count in range(0,response,1):
  steps_remaining = response - count
  print(f"{steps_remaining} steps remaining")
print("we have reached the cave!")