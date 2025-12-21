class  chennai: 
    name="vfds"             #first name register
    movie=""
    def party(self): #varun
        print("Lets party.....")
    def beach(self):
        print("Enjoying the beach")

varun = chennai()                    #Access the object's properties in the class
arun = chennai()

varun.name="Varun"                   #registered the name/set the name
arun.name="Arun"

varun.movie="yes"
arun.movie="no"

print(varun.name)                                                                #arun.party()
print("movie:",varun.movie)

print(arun.name)
print("movie:",arun.movie)                                                                #varun.beach()

varun.party()
arun.beach()
