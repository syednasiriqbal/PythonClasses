#### Time in Video 29:30 - Before that there is OOPS Introduction ####

# def person():
#     print("hello")
  
  
class Person: # class name should starts with uppercase 
    
    ''' This class is defined for Person info '''   #Doc String 
    
    name='Raja'
    age=45
    country='India'
    
    #Actions
    def speak(self):    #Method #Instance Method
        print("English")
        
    def write(self):
        print("he writes in English")
           
objref=Person()  # create an object and assigned reference variable
 
objref.write()  # accessing the instance methods by using object refer
objref.speak()

print(objref.name) # accessing the variables by using the object reference
print(objref.age)
print(objref.country)

print(Person.__doc__)