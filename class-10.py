 # learning Class

class MyClass:
    pass

instance_1 = MyClass()
instance_1.xyz= "ASAs"
print(instance_1.xyz)


class JawanPakistanAdmissionForm:
    # class Attributes
    contact ="+92342"
    
    # somthing like constructor 
    def __init__(self,name,dob,nic):
        self.name =name
        self.dob =dob
        self.nic =nic

    def get_all_detail(self):
        print("All Details" ,self.__dict__)
        print(self.name,self.contact)

    @classmethod # usually used when creeating object
    def get_all_detail_cls(cls):
        print("All Details" ,cls.__dict__)
        print(cls.contact,cls.contact)

amjad_form = JawanPakistanAdmissionForm("Amjad","2000-08-25","32424834924")
print(amjad_form) # will prin memorry adddress thay would also be same for slef
print(amjad_form.__dict__) # will print dictionary style

amjad_form.get_all_detail()
amjad_form.get_all_detail_cls()



class Employee:

    def __init__(self,fname,lname,gender,salary,joining_date):
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.salary=salary
        self.joining_date=joining_date
    
    def get_salary(self):
        return self.salary

class Driver(Employee):

    def __init__(self, fname, lname, gender, salary, joining_date, lic_no):
        super().__init__(fname, lname, gender, salary, joining_date)
        self.lic_no=lic_no
    
    def get_salary(self,num_days):
        return (int(self.salary)/30)*num_days

amjad_driver=Driver("Amjad","Khan","Male","100000","2024-03-25","3435343")
print("Salary of Amjad Driver ",amjad_driver.get_salary(23))

