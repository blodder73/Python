message = input("Tell me something, and I will repeat it back to you: ")
print(message)

print()
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

print()
prompt = "if you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")