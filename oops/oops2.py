class Student:
    school_name = "XYZ School"

    def set_details(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)
        print(Student.school_name)



obj = Student()
obj.set_details("Vamsi", 85)
obj.display()


class Employee:
    company = "Infosys"

    def set_data(self,name,salary):
        self.name = name
        self.salary = salary 
    
    def increase_salary(self):
        self.salary = self.salary + 5000

    def display(self):
        print(self.name)
        print(self.salary)
        print(Employee.company)

a = Employee()
a.set_data("Ravi",20000)
a.increase_salary()
a.display()


class Mobile:
    brand = "Apple"

    def set_details(self,model,price):
        self.model = model
        self.price = price

    def discount(self):
        self.price = self.price - self.price/100 * 10

    def show_details(self):
        print(self.brand)
        print(self.price)
        print(Mobile.brand)

b = Mobile()
b.set_details("Iphone", 80000)
b.discount()
b.show_details()