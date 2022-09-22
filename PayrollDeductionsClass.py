class PayrollDeductions:
    def __init__(self, description, date, charge, employeeID):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__employeeID = employeeID

    def get_desc(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge
    
    def get_employee_ID(self):
        return self.__employeeID