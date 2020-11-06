print("What strange markings do you see?")
response = input()
count = 0
print("Identifying...")
for position in range(0,len(response),1):
 print(f"index {count}:"+response[position])
 count+=1
print("Done!")