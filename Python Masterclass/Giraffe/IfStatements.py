is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")


is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are not a male nor tall")


is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male or not tall")