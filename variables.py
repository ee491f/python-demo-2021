numberVariable = 3.3
print(numberVariable)
numberVariable = 3
print(numberVariable)

stringVariable = 'hello'
print(stringVariable)
stringVariable = "hello"
print(stringVariable)

listVariable = [
  1,
  "two",
  3.3,
  [
    'yo',
    'dude',
  ],
  1,
]
print(listVariable)
print(listVariable[2])


setVariable = set([
  1,
  "two",
  3.3,
  1,
])
print(setVariable)

dictVariable = {
  "key": "value",
  stringVariable: "string value",
  "string key": stringVariable,
  "list": listVariable,
}
print(dictVariable)