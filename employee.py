"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class BasicSalaryWorker(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return(f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}')



class BasicContractWorker(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def get_pay(self):
        return self.rate * self.hours

    def __str__(self):
        return(f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour. Their total pay is {self.get_pay()}')



class SalaryContractCommission(Employee):
    def __init__(self, name, salary, commContracts, commRate):
        super().__init__(name)
        self.salary = salary
        self.commContracts = commContracts
        self.commRate = commRate

    def get_pay(self):
        return self.salary + self.commContracts * self.commRate

    def __str__(self):
        return(f'{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.commContracts} contracts(s) at {self.commRate}/contract. Their total pay is {self.get_pay()}')



class ContractContractCommission(Employee):
    def __init__(self, name, hours, rate, commContracts, commRate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.commContracts = commContracts
        self.commRate = commRate

    def get_pay(self):
        return self.hours * self.rate + self.commContracts * self.commRate

    def __str__(self):
        return(f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.commContracts} contracts(s) at {self.commRate}/contract. Their total pay is {self.get_pay()}')

class SalaryBonusCommission(Employee):
    def __init__(self, name, salary, commBonus):
        super().__init__(name)
        self.salary = salary
        self.commBonus = commBonus

    def get_pay(self):
        return self.salary + self.commBonus

    def __str__(self):
        return(f'{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commBonus}. Their total pay is {self.get_pay()}')

class ContractBonusCommission(Employee):
    def __init__(self, name, hours, rate, commBonus):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.commBonus = commBonus

    def get_pay(self):
        return self.rate * self.hours + self.commBonus

    def __str__(self):
        return(f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.commBonus}. Their total pay is {self.get_pay()}')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = BasicSalaryWorker('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = BasicContractWorker('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContractCommission('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractContractCommission('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonusCommission('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractBonusCommission('Ariel', 120, 30, 600)
