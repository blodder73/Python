t = ("a", "b", "c")
print(t)

name = "Tim"
age = 10
print("\n")
print(name, age, "Python", 2020)
print((name, age, "Python", 2020))

print("\n")

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Copmany", "Bad Copmany", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lightning", "Metallica", 1984),
          ]

print(len(albums))
for album in albums:
    print("Album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))

print()

for name, artist, year  in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))