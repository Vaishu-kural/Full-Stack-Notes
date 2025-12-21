class student:
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("\nName:",self.name)
        print("Register Number:",self.regno)

s1=student()
s2=student()

s1.name="Jeeva"
s1.regno="001"

s2.name="Janani"
s2.regno="002"

s1.display()
s2.display()
