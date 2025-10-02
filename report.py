import os
import webbrowser

from fpdf import FPDF


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

        #Add icon image
        pdf.image("./assets/house.png", w=30, h=30)

        #Insert title
        pdf.set_font(family='Arial', style='B', size=22)
        pdf.cell(0, 80, txt="Flatmates Bill", align="C", ln=1)

        #Insert Period label and value
        pdf.set_font(family='Arial', style='B', size=14,)
        pdf.cell(80, 40, txt="Period: ")
        pdf.cell(150, 40, txt=bill.period, ln= 1)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family='Arial', size=14)
        pdf.cell(80, 40, txt=flatmate1.name)
        pdf.cell(80, 40, txt=str(flatmate1.pays(bill, flatmate2)), ln=1)

        #Insert name and due amount of the second flatmate
        pdf.cell(80, 40, txt=flatmate2.name)
        pdf.cell(80, 40, txt=str(flatmate2.pays(bill, flatmate1)), ln=1)

        #Save pdf
        relative_filename_path = f"assets/{self.filename}"
        pdf.output(relative_filename_path)
        webbrowser.open('file:///'+os.path.realpath(relative_filename_path))
