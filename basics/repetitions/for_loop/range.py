print("What level of brightness is required?")
response = int(input())
print("Adjusting brightness")
counter = 1
for count in range (0, response, 2):
 Brightness = "**"*counter
 print("Beeps's bringtness level:"+Brightness+"\n")
 print("Bop's bringtness level:"+Brightness+"\n")
 counter+=1
print("Adjustment complete!")