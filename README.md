# Ethical Link — Loan & Installment Planner

A professional web-based financial tool built with Python and Flask that helps 
users plan loan repayment schedules. Supports both Islamic interest-free loans 
and standard fixed installment plans.

---

## Features

- Islamic Interest-Free Calculator (Qard al-Hasan) with zero interest
- Standard Installment Plan calculator with compound interest support
- Live month by month repayment schedule table
- Automatic PKR number formatting with comma separators
- Quick duration selector pills for common loan periods (3, 6, 12, 24, 36, 48, 60, 120 months)
- Manual duration input for custom repayment periods
- Smooth loan type toggle between Islamic and Standard plans
- Interest rate field that shows and hides based on selected loan type
- Summary box showing total payable and monthly installment after calculation
- Save repayment schedule as a CSV file with one click
- Clear Form button to instantly reset all inputs
- Page clears automatically on refresh with no stale data
- Fully responsive layout that works on mobile and desktop
- Professional dark navy and emerald green design theme

---

## Tech Stack

- Python 3.13
- Flask 3.1.3
- HTML5 and CSS3
- Vanilla JavaScript
- Jinja2 Templating Engine

---

## Project Structure
```
Ethical Link/
├── templates/
│   └── index.html        # Main application page
├── static/
│   └── styles.css        # All styling and animations
├── app.py                # Flask server and calculation logic
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

---
## Live Demo

🌐 [https://ethical-link.onrender.com](https://ethical-link.onrender.com)

> Note: Please allow up to 60 seconds for the initial load as the app
> is hosted on a free tier server that spins down during inactivity.

## How to Run Locally

1. Clone the repository
```
   git clone https://github.com/shayanali1/Ethical Link.git
```

2. Navigate into the project folder
```
   cd Ethical Link
```

3. Create a virtual environment
```
   py -m venv venv
```

4. Activate the virtual environment
```
   venv\Scripts\activate
```

5. Install dependencies
```
   py -m pip install -r requirements.txt
```

6. Run the application
```
   py app.py
```

7. Open your browser and visit
```
   http://127.0.0.1:5000
```

---

## Calculations

**Islamic Interest-Free Plan**
```
Monthly Installment = (Principal + Service Charge) / Duration
Total Payable = Principal + Service Charge
Interest Paid = 0
```

**Standard Installment Plan**
```
Monthly Rate = Annual Interest Rate / 100 / 12
Monthly Installment = (Principal × Monthly Rate) / (1 - (1 + Monthly Rate) ^ -Duration)
Total Payable = Monthly Installment × Duration
Interest Paid = Total Payable - Principal
```

---

## Author

**Syed Muhammad Shayan Ali**   
[GitHub](https://github.com/shayanali1)

---


## License

This project is open source and available for educational and personal use.