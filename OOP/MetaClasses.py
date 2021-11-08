class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f'Creating new instance of {name}')
        print(attrs)
        
        new_instance = super().__new__(cls, name, bases, attrs)
        return new_instance

        

class InputRestrictor:
    def __init__(self, v1, v2):
        if v1 > 10:
            self.v1 = 10
        else:
            self.v1 = v1

        if v2 > 10:
            self.v2 = 10
        else:
            self.v2 = v2

    
    
class TestClass(InputRestrictor, metaclass = Meta):
    def print_values(self):
        print(f'{self.v1}, {self.v2}') 

    

    
if __name__ == '__main__':
    obj = TestClass(11, 2)
    obj.print_values()
