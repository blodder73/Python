computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])
print(computer_parts[0:3])
print(computer_parts[-1])


# for index, part in enumerate(computer_parts):
#     print(str(index) + ". " + part)

print("\n")
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)
#computer_parts[3] = "Trackball"
print(computer_parts[3:])

computer_parts[3:] = "trackball"
print(computer_parts)
computer_parts[3:] = ["trackball"]
print(computer_parts)

