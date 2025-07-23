class Employee:
    def __init__(self, name, salary, company, tax_percent, profit_percent):
        company = "Infosys"  
        salary = 50000       
        tax_percent = 10     
        profit_percent = 5   

        self.name = name
        self.salary = salary
        self.company = company
        self.tax_percent = tax_percent
        self.profit_percent = profit_percent
        self.tax = (self.tax_percent / 100) * self.salary
        self.profit_share = (self.profit_percent / 100) * self.salary

    def display_info(self):
        print("\nEmployee Details:")
        print(f"Name          : {self.name}")
        print(f"Company       : {self.company}")
        print(f"Salary        : {self.salary}")
        print(f"Tax to Pay    : {self.tax}")
        print(f"Profit Share  : {self.profit_share}")



emp = Employee("Alice", 0, "", 0, 0)
emp.display_info()
