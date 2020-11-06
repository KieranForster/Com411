def escape(route):
    if (route == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif (route == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif (route == "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("Not sure about that route!")
escape("jumping over")
escape("running around")
escape("going deeper") 