print("Hello!")
print("Is it Alfonso you're looking for?")

name = ["hi", 1]  # list
name.append("dog")  # append to the list

print("name:", name)

my_set = {}  # makes a dictionary! Must use my_set = set()
my_set = {"foo", "bar", "foo"}
my_set.add("monkey")
my_set.update({"baz", "hello", "345", "foo fighter"})

print("my set:", my_set)


zoo = ("dog", "Fred", "cuttlefish")

# no implicit coercion
print("4" + str(3))
print(int("4") + 3)

cow = "moo"
dog = "woof"
if cow == "moo" and dog == "woof":
    print(cow)
elif cow == "Woof":
  print("WTF?")
else:
    print("The End")


for thing in my_set:
  print(thing.title())

# for item in my_set:
#   for animal in zoo:
#     print("I like to take my {0} to see the {1} at the zoo".format(item, animal))


person = {
  "name": "Fred",
  "age": 34,
}

for trait in person.items():
  print(trait)

# both key and value
for key, trait in person.items():
  print(key, trait)

list_of_stuff = ["stuff", "things", "junk", "candy bar"]
print( (" ... ").join(list_of_stuff))

#JS way
# list_of_stuff.join(" ... ")

# functions
foo = "monkeys"
def do_something(foo):
  if foo == "monkeys":
    print("I like " + foo)
    return
  print("Something else " + foo)

do_something("monkeys")

#named arguments and positional arguments

# scope

name = "Fred"

# def say_name():
#   name = "Sally"
#   print("inside name", name)

def say_name():
  global name
  name = "Sally"
  print("inside name", name)

say_name()
print("outside name", name)