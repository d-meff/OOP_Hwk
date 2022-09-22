class Employee:
    def __init__(self, name, IDnumber, department, title, monthlySalary):
        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department
        self.__title = title
        self.__monthlySalary = monthlySalary

    def get_name(self):
        return self.__name

    def get_ID_number(self):
        return self.__IDnumber

    def get_department(self):
        return self.__department
    
    def get_title(self):
        return self.__title

    def get_monthly_salary(self):
        return self.__monthlySalary