from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_emi(principal, rate_of_interest, tenure):
    """
    Calculate EMI for a loan.

    Parameters:
    principal (float): Loan amount
    rate_of_interest (float): Annual interest rate (in percentage)
    tenure (int): Loan tenure in months

    Returns:
    float: EMI amount
    """
    if rate_of_interest == 0:
        return principal / tenure

    monthly_interest_rate = (rate_of_interest / 100) / 12
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate)**tenure) / \
          ((1 + monthly_interest_rate)**tenure - 1)
    return emi

@app.route('/', methods=['GET', 'POST'])
def index():
    emi = None
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            rate_of_interest = float(request.form['rate_of_interest'])
            tenure = int(request.form['tenure'])

            emi = calculate_emi(principal, rate_of_interest, tenure)
        except (ValueError, ZeroDivisionError):
            emi = "Invalid input! Please ensure all inputs are correct."

    return render_template('index.html', emi=emi)

if __name__ == '__main__':
    app.run(debug=True)
