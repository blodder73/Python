lucky_numbers = [32, 4, 42, 15, 16, 3, 2]
friends = ["Kevin", "karin", "Jim", "Oscar", "Oscar", "Toby"]

print(friends)
friends.extend(lucky_numbers)

friends = ["Kevin", "karin", "Jim", "Oscar", "Oscar", "Toby"]

print(friends)

friends.append("Jenny")
print(friends)

friends.insert(1,"Kelly")
print(friends)

friends.remove("Jim")
print(friends)


print(friends[1])
print(friends[-1])
print(friends[1:3])
friends[1] = "Buddy"
print(friends[1])

friends.pop()
print(friends)

print(friends.index("Oscar"))
print(friends.count("Oscar"))

friends.sort()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers.sort(reverse=True)
print(lucky_numbers)

friends2 = friends
print(friends2)

friends.clear()
print(friends)

