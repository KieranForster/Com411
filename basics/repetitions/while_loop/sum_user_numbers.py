print("how many numbers should i sum up?")
response = int(input())
count = 1
number_sum = 0
while count <= response:
 print(f"Please enter number {count} of {response}:")
 number = int(input())
 number_sum = number+number_sum
 count+=1
print(f"The answer is {number_sum}")