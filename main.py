from flat import Bill, Flatmate
from report import PdfReport

bill_amount = float(input("Enter the bill amount: "))
bill_period = input("Enter the period of the bill E.g December 2020: ")

bill = Bill(amount=bill_amount, period=bill_period)

flatmate1_name = input("Enter the name of for the first flatmate: ")
flatmate1_days_in_house = int(input(f"Enter the number of days {flatmate1_name} stayed in the house: "))
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days_in_house)

flatmate2_name = input("Enter the name of days for the second flatmate: ")
flatmate2_days_in_house = int(input(f"Enter the number of days {flatmate2_name} stayed in the house: "))
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days_in_house)


print(f"{flatmate1.name} pays:", flatmate1.pays(bill, flatmate=flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(bill, flatmate=flatmate1))

pdf_report = PdfReport("Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)