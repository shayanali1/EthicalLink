from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    principal = float(request.form["principal"])
    duration = int(request.form["duration"])
    charge = float(request.form["charge"])
    loan_type = request.form["loan_type"]

    if loan_type == "islamic":
        monthly_installment = (principal + charge) / duration
        total_payable = principal + charge
        interest_paid = 0

    else:
        interest_rate = float(request.form["interest_rate"])
        monthly_rate = interest_rate / 100 / 12
        monthly_installment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -duration)
        total_payable = monthly_installment * duration
        interest_paid = total_payable - principal

    return render_template("result.html",
        principal=principal,
        duration=duration,
        loan_type=loan_type,
        monthly_installment=round(monthly_installment, 2),
        total_payable=round(total_payable, 2),
        interest_paid=round(interest_paid, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)