# Comprehensions
flowers = {'Lily', 'Snapdragon', 'Rose', 'Lily', 'Tulip'}
bees = ['bumblebee', 'honeybee', 'Barnaby']

# flowers_quotes = list()
# for flower in flowers:
#   flowers_quotes.append(f"{flower}s make me sneeze.")

flowers_quotes = {f"{flower}s make me sneeze" for flower in flowers}
# print(flowers_quotes)

# large_flowers = []
# for flower in flowers:
#   for bee in bees:
#     large_flowers.append(f"The {bee} pollinates the {flower}.")

# print(large_flowers)


larger_flowers = [f"The {bee} pollinates the {flower}." for flower in flowers for bee in bees]
print(larger_flowers)