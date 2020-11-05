print("Please enter number of lives")
lives = int(input())
print("Please enter the engery level")
energy_level = int(input())
print("Please enter the sheild level")
sheild_level = int(input())
lives_display = "♥"
energy_display = "♦"
print("Health has been set!\n\n Lives:   {}\n Energy:  {}\n Sheild:  {}".format(lives_display*lives,energy_display*energy_level,energy_display*sheild_level))