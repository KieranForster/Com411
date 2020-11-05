print("how many live cables must i avoid?")
response = int(input())
avoided_cables=0
while response > avoided_cables:
 print(f"Avoidoing. . . Done! {avoided_cables} live cables avoided.")
 avoided_cables+=1
print("All live cables have been avoided.")