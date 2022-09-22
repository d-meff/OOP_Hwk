class Employee:
    def __init__(self, name, ID, number, department, title):
        self.__name = name
        self.__ID = ID
        self.__number = number
        self.__department = department
        self.__title = title

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_number(self):
        return self.__number

    def get_department(self):
        return self.__department
    
    def get_title(self):
        return self.__title