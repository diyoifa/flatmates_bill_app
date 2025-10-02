# 🏠 Flatmates Bill

## 📌 Description
**Flatmates Bill** is a small CLI app that helps split a household bill fairly between flatmates.  
It takes as input:  
- The **total amount** of a bill for a given period.  
- The **number of days** each flatmate stayed in the house during that period.  

The app calculates how much each flatmate has to pay and generates a **PDF report** including:  
- The names of the flatmates.  
- The billing period.  
- Each flatmate's share of the bill.  

---

## 🎯 Main Objects

### `Bill`
- **Attributes:**
  - `amount` → total bill amount.
  - `period` → billing period (e.g., "March 2025").
  
### `Flatmate`
- **Attributes:**
  - `name` → flatmate’s name.
  - `days_in_house` → number of days the flatmate stayed.  
- **Methods:**
  - `pays(bill)` → returns the share of the bill for this flatmate.  

### `PdfReport`
- **Attributes:**
  - `filename` → output PDF file name.  
- **Methods:**
  - `generate(flatmate1, flatmate2, bill)` → creates a PDF with the payment details.  

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/flatmates-bill.git
cd flatmates-bill
pip install -r requirements.txt
