from fpdf import FPDF


class Bill:
    """
    Object that contains information about a bill,
    such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


    def pays(self, bill, flatmate):
        total_days = self.days_in_house + flatmate.days_in_house
        weight = self.days_in_house/total_days
        return  weight * bill.amount

class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    such as their names, their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Insert title
        pdf.set_font('Arial', 'B', 22)
        pdf.cell(0, 80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Insert label and value
        pdf.cell(80, 40, txt="period", border=1)
        pdf.cell(150, 40, txt=bill.period, border=1, ln=1)

        #Insert name and due amount of the first flatmate
        pdf.cell(80, 40, txt=flatmate1.name, border=1)
        pdf.cell(80, 40, txt=str(flatmate1.pays(bill, flatmate2)), border=1)

        #Insert name and due amount of the second flatmate
        pdf.cell(80, 40, txt=flatmate2.name, border=1)
        pdf.cell(80, 40, txt=str(flatmate2.pays(bill, flatmate1)), border=1)

        #Save pdf
        pdf.output(self.filename)


bill = Bill(amount=10000, period="March 2025")
john = Flatmate(name="John", days_in_house=12)
marry = Flatmate(name="Mary", days_in_house=20)

print("John pays:", john.pays(bill, flatmate=marry))
print("Mary pays:", marry.pays(bill, flatmate=john))

pdf_report = PdfReport("Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)