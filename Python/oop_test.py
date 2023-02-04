from datetime import date
from pydoc import describe
class Students :
    
    def __init__ (self , name , age ) :
        self.name  = name 
        self.age = age 
       

    def describe (self) :
        print (f"my name is {self.name} and my age is {self.age}") 

    
    
    @classmethod 

    def  initFromBirthYear(cls , name , birthyear ) : 
        return cls(name , date.today().year - birthyear )



student1 = Students.initFromBirthYear('aymen' , 2003)
student1.describe()






    
        

    
    
    

  




























        
    