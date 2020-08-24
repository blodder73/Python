activity = input("What would you like to do today? ")

if "cinema" not in activity.lower():
    print("I don't want to {}, I want to go to the cinema".format(activity))
else:
    print("I will come with you to the {}!".format(activity))