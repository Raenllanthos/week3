class ROI():
    def __init__(self, property = 0, income = 0, expenses = 0, totalInvestment = 0):
        self.property = property
        self.income = income
        self.expenses = expenses
        self.totalInvestment = totalInvestment

    def getProperty(self):
        return int(input("How much was the property originally? "))
    
    def getIncome(self):
        return int(input("How much is your monthly income? "))

    def getExpenses(self):
        return int(input("How much are your monthly expenses? "))

    def getInvestment(self):
        return int(input("\nIncluding down payments, and closing costs\nHow much have you spent on this property? "))

    def cashFlow(self):
        return (12 * (self.income - self.expenses))

    def math(self):
        print(f"\nYour yearly cash flow is: ${self.cashFlow()}\nYour total investment is: ${self.totalInvestment}")
        roi = 100 * ((self.cashFlow()) / self.totalInvestment)
        print(f"Your purchased the house for: ${self.property},\nYour yearly ${self.cashFlow()}", 
        f"investment on your ${self.totalInvestment} property is {roi}%")

def main():
    ROI(ROI().getProperty(), ROI().getIncome(), ROI().getExpenses(), ROI().getInvestment()).math()

main()
