class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.speak())
# Duck typing in action:
d = Dog()
c = Cat()
animal_sound(d)  # Output: Woof!
animal_sound(c)  # Output: Meow!
#animal_sound()
