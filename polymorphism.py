class Animal:
    def speak(self):
       pass
   
   
class Dog(Animal):
    def speak(self):
        print("barks")
        
class Cat(Animal):
    def speak(self):
        print("meows")
        
class Cow(Animal):
    def speak(self):
        print("moo")
        

dog= Dog()
cat= Cat()
cow= Cow()

dog.speak()
cat.speak()
cow.speak()