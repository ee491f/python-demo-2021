listVariable = [
  1,
  "two",
  3.3,
  1,
  [
    'yo',
    'dude',
  ]
]

print("looping through a list")
for listItem in listVariable:
  print(listItem)
print("looping through a list again")
for index, listItem in enumerate(listVariable):
  print(index)
  print(listItem)

stringVariable = "hello"
dictVariable = {
  "key": "value",
  stringVariable: "string value",
  "string key": stringVariable,
  "list": listVariable,
}

print("looping through a dictionary")
for dictKey, dictValue in dictVariable.items():
  print("===")
  print("key")
  print(dictKey)
  print("value")
  print(dictValue)
