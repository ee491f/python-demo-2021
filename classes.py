class MyClass:
  classVariable = "class variable"

  def class_method():
    print("class method called")

  def __init__(self):
    self.instanceVariable = "instance variable"

  def instance_method(self):
    print("instance method called")
    print(self.instanceVariable)

classInstance = MyClass()
classInstance.instance_method()
MyClass.class_method()
print(MyClass.classVariable)