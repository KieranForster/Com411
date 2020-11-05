print("Please enter a number?")
response = int(input())
count = 0
answer = 0
while count < response:
 answer = answer + count
 count+=1
print(f"The factoral is {answer}")