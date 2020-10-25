dinner_group = input("How many people in the dinner group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print(f"your group is larger than 8 people, you have {dinner_group} people. You'll have to wait")
else:
    print(f"Table is ready")