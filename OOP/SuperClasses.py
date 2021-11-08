class Person: 

    def __init__(self, gender, age, race, height): 

        self.gender = gender 

        self.age = age 

        self.race = race 

        self.height = height 

         

    def say_hello(self): 

        print(f'Hello I am a {self.gender}') 

         

         

  

  

class Male(Person): 

    #modification of __init__ method from superclass 

    def __init__(self, age, race, height): 

        super().__init__('male', age, race, height) 

     

    #method extension 

    def say_hello(self): 

        super().say_hello() 

        print('Called from a child class') 

         

     

     

         

if __name__ == '__main__': 

    male = Male(10, 'white', 180) 
    male.say_hello() 
