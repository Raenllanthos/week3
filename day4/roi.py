class ROI():
    def __init__(self, income = 0, expenses = 0, totalInvestment = 0):
        self.income = income
        self.expenses = expenses
        self.totalInvestment = totalInvestment
    
    def getIncome(self):
        return int(input("How much is your monthly income? "))

    def getExpenses(self):
        return int(input("\nHow much are your monthly expenses? "))

    def getInvestment(self):
        return int(input("\nIncluding down payments, and closing costs\nHow much have you spent on this property? "))

    def cashFlow(self):
        return (12 * (self.income - self.expenses))

    def math(self):
        print(f"\nYour yearly cash flow is: ${self.cashFlow()}\nYour total investment is: ${self.totalInvestment}")
        roi = 100 * ((self.cashFlow()) / self.totalInvestment)
        print(f"Your yearly ${self.cashFlow()} investment on your ${self.totalInvestment} property", 
        f"is {roi}%")

def main():
    ROI(ROI().getIncome(), ROI().getExpenses(), ROI().getInvestment()).math()

main()
