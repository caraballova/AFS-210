class Employee ():
    def __init__(self, fName, lName, eID, hourlyPay):
        self.fName = fName
        self.lName = lName
        self.eID = eID
        self.hourlyPay = hourlyPay

    def pay(self, hours):
        self.hours = hours
        if hours <= 40:
            return hours*self.hourlyPay
        elif hours > 40:
            return (40*self.hourlyPay)+((hours-40)*self.hourlyPay*1.5)




fName = input("Please enter Employee's first name : ")
lName = input("Please enter Employee's last name : ")
eID = int(input("What is the Employee's ID Number? "))
hourlyPay = float(input("Please enter the employee's pay rate : "))
hours = float(input("How many hours did this employee work? "))
newEmployee = Employee(fName, lName, eID, hourlyPay)


print(fName + " " + lName + "s total pay for the week is $ " + str(newEmployee.pay(hours)) + " \U0001f600")