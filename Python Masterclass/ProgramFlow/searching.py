shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# for index in range(6)
# for index in range(len(shopping_list)):
#     print("{}. {}".format(index + 1, shopping_list[index]))
#     if shopping_list[index] == item_to_find:
#         found_at = index
# print("Item {} found at position {}".format(item_to_find, found_at + 1))

# print("\n\n")
# for index in range(len(shopping_list)):
#     print("{}. {}".format(index + 1, shopping_list[index]))
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# print("Item {} found at position {}".format(item_to_find, found_at + 1))

# -------------------------------------------------------

# item_to_find = "albatross"

# for index in range(len(shopping_list)):
#     print("{}. {}".format(index + 1, shopping_list[index]))
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item {} found at position {}".format(item_to_find, found_at + 1))
else:
    print("{} not found".format(item_to_find))