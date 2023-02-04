class Employee :
    def __init__(self , name , age , place , is_manager , rating , salary  ):
        self.name = name 
        self.age = age 
        self.place  = place
        self.is_manager = is_manager 
        self.rating = rating 
        self.salary = salary 

    def is_exellent (self):
        if self.rating >= 4.5 : 
            return True

        else : 
            return False 

    def bonus (self) : 
        if self.age >= 60 : 
            self.salary += 500 
            print("your salary incresed to "  + str (self.salary) )

        else : 
            
            print("your  salary stay the same " + str (self.salary))




        
           
    