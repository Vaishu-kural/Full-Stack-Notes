class laptop:
    ram=""
    processor=""
    def __init__(self):
        self.ram=""
        self.processor=""
        #print("demo")
    def display(self):                  #self --> current object(hp)
        print("Ram:",self.ram)
        print("Processor:",self.processor)

hp=laptop()
dell=laptop()

hp.ram="8GB"
hp.processor="i5"

dell.ram="16GB"
dell.processor="i7"

hp.display()                                     #hp.display(hp)
dell.display()
