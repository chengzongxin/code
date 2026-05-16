class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("hello, my name is" + self.name)

    def say_hello_to(self, name):
        print("hello, my name is "+ self.name + "hello" + name)


person1 = Person("eren", 18)
person2 = Person("mikasa", 17)
person3 = Person("sasha", 16)
person4 = Person("luffy", 15)

person1.say_hello()
person2.say_hello()
person3.say_hello()
person4.say_hello()

person1.say_hello_to(person2.name)
