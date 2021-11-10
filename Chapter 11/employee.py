class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number
    def set_name(self):
        self.__name = name
    def set_id_number(self):
        self.__id_number = id_number
    def get_name(self):
        return self.__name
    def get_id_number(self):
        return self.__id_number

class ProductionWorker(Employee):
    def __init__(self, name, id_number, number_s, tax):

        Employee.__init__(self, name, id_number)

        self.__number_s = number_s
        self.__tax = tax

    def set_number_s(self, number_s):
        self.__number_s = number_s

    def set_tax(self, tax):
        self.__tax = tax

    def get_number_s(self):
        return self.__number_s

    def get_tax(self):
        return self.__tax

class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, year_pay, year_prize):

        Employee.__init__(self, name, id_number)
        self.__year_pay = year_pay
        self.__year_prize = year_prize

    def set_year_pay(self, year_pay):
        self.__year_pay = year_pay
    def set_year_prize(self, year_prize):
        self.__year_prize = year_prize

    def get_year_pay(self):
        return self.__year_pay

    def get_year_prize(self):
        return self.__year_prize








