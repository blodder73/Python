data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for index, item in enumerate(data):
    if item.endswith("Flower"):
        flowers.append(item)
    elif item.endswith("Shrub"):
        shrubs.append(item)

print("{0} flowers and {1} shrubs.".format(len(flowers), len(shrubs)))

print("\nFLOWERS")
for flower_index, flower in enumerate(flowers):
    print("{0}: {1}".format(flower_index + 1, flower))

print("\nSHRUBS")
for shrub_index, shrub in enumerate(shrubs):
    print("{0}: {1}".format(shrub_index + 1, shrub))