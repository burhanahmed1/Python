# Create a class ‘Employee’ and add salary and increment properties to it.

'''
Write a method salaryAfterIncrement method with a @property decorator with a setter 
which changes the value of increment based on the salary.
'''

class Employee:
    salary=0
    increament=0

    @property
    def salaryafterincreament(self):
        return (self.salary + (self.salary*(self.increament/100)))
    
    @salaryafterincreament.setter
    def salaryafterincreament(self,salary):
        self.increament=((salary/self.salary)-1)*100

    def show(self):
        print(f"The old salary was {self.salary} and the salary after {self.increament}% increament is {self.salaryafterincreament}.")


e=Employee()
e.salary=500000
e.increament=20
e.show()
e.salaryafterincreament= 650000
print(f"The Increament is of {e.increament}%")

        
