class Demo:
    def greet(self, name=None):
        if name:
            print("Hello " + name)
        else:
            print("Hello")

d = Demo()
d.greet()        # Hello
d.greet("John")  # Hello John
