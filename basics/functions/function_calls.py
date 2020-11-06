print("Please enter a word.")
word = input()
def display_box(word):
  print("##"+"#"*len(word)+"##")
  print("# "+word+" #")
  print("##"+"#"*len(word)+"##")
def display_lower(word):
  print(word.lower())
def display_upper(word):
  print(word.upper())
def display_mirrored(word):
  reverse_word = str()
  for letter in reversed(word):
    reverse_word+=letter
    print("{} | {}".format(word, reverse_word))
def repeat():
  print("please enter the amount of repitiions.")
  multiplier = input()
  print((word+"\n")*multiplier)
def run():
  print("Please choose and option.\n")
  print("display in a box 1\n")
  print("display lower case 2\n")
  print("display in upper case 3\n")
  print("display mirrored 4\n")
  print("repeat 5\n")
  decision = input()
  if decision == "1":
   display_box(word)
  elif decision == "2":
   display_lower(word)
  elif decision == "3":
   display_upper(word)
  elif decision == "4":
   display_mirrored(word)
  elif decision == "5":
   repeat()
  else:
    print("tis fucked") 
run()