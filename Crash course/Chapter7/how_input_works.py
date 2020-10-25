prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)



#
# print()
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
#
# print()
# prompt = "if you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "
#
# name = input(prompt)
# print(f"Hello, {name}!\n")

height = input("How tall are you? ")
height = int(height)

if height >= 160:
    print("\nYou're tall enough for the ride\n\n")
else:
    print("\nYou'll be able to ride when you're older.\n\n")

number = input("Enter a number, and I'll tell you if it's odd or even: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


