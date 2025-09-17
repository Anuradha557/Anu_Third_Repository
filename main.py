class Employee:
    def __init__(self,emp_id,emp_name,emp_designation):
        self.emp_id=emp_id
        self.emp_name = emp_name
        self.emp_designation= emp_designation
    def emp_info(self):
        print("Employee Id--->",self.emp_id)
        print("Employee Name--->",self.emp_name)
        print("Employee designation--->",self.emp_designation)
        print("print data successfully\n")

emp_obj1=Employee(5080180,'Anu','developer')
emp_obj2=Employee(5090180,'Tejaswini','Tester')
emp_obj3=Employee(5082500,'Renu','Frontend Developer')
emp_obj1.emp_info()
emp_obj2.emp_info()
emp_obj3.emp_info()