import json
import warlock
import numpy

with open("schema.json") as json_data:
    schema = json.load(json_data)

IBlock = warlock.model_factory(schema)
first = IBlock(name = "first", children = [])
second = IBlock(name = "second", children = [])
list = [first, second]
third = IBlock(name = "third", children=list)

print("first", first.name)
print("second", second.name)
print("third", third.name)
print("third's chil", third.children)
print("third's first chil", third.children[0].name)
print("third's type", type(third))
print("third's chil type", type(third.children[1]))
print(type(third) == type(third.children[1]))
print(type(third) == type(third.children[0]))

listlist = [39, 180, 71, 18, 59, 70, 426, 30, 57, 102]
print(numpy.mean(listlist))
print(numpy.std(listlist))