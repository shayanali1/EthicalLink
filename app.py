from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "ethicallink_secret_key"

@app.route("/", methods=["GET"])
def home():
    results = session.pop("results", None)
    schedule = session.pop("schedule", [])
    return render_template("index.html", results=results, schedule=schedule)

@app.route("/calculate", methods=["POST"])
def calculate():
    principal = float(request.form["principal"].replace(",", ""))
    duration = int(request.form["duration"])
    charge = float(request.form["charge"].replace(",", ""))
    loan_type = request.form["loan_type"]

    if loan_type == "islamic":
        monthly_installment = (principal + charge) / duration
        total_payable = principal + charge
        interest_paid = 0
    else:
        interest_rate = float(request.form["interest_rate"])
        monthly_rate = interest_rate / 100 / 12
        monthly_installment = (principal * monthly_rate) / (
            1 - (1 + monthly_rate) ** -duration
        )
        total_payable = monthly_installment * duration
        interest_paid = total_payable - principal

    results = {
        "principal": f"{principal:,.2f}",
        "duration": duration,
        "loan_type": loan_type,
        "charge": f"{charge:,.2f}",
        "monthly_installment": f"{monthly_installment:,.2f}",
        "total_payable": f"{total_payable:,.2f}",
        "interest_paid": f"{interest_paid:,.2f}",
    }

    schedule = []
    remaining_balance = principal
    principal_per_month = principal / duration

    for month in range(1, duration + 1):
        if month == duration:
            principal_paid = remaining_balance
        else:
            principal_paid = principal_per_month
        remaining_balance -= principal_paid
        schedule.append({
            "month": month,
            "principal_paid": f"{principal_paid:,.2f}",
            "monthly_installment": f"{monthly_installment:,.2f}",
            "remaining_balance": f"{max(0, remaining_balance):,.2f}",
        })

    session["results"] = results
    session["schedule"] = schedule
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)