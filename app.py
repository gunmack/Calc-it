from flask import Flask, render_template, request, redirect, url_for
from functions import evaluate_expression

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('numberpad'))

@app.route("/calculator", methods=["GET", "POST"])
def numberpad():
    expression = request.form.get("expression", "")
    result = ""
    recall = expression [:]

    if request.method == "POST":
        if 'delete' in request.form:
            # x = len(expression)
            expression = expression[:-1]

        if 'clear' in request.form:
            expression = ""
            result + ""
        elif 'recall' in request.form:
            expression = recall [:]
        else:
            if expression:
                try:
                    # TODO: import and use own functions instead of eval (done)
                    # result = eval(expression)
                    result = evaluate_expression(expression)
                    expression = result
                    recall = expression [:]
                except Exception as e:
                    result = "Error"

    return render_template('numberpad.html', expression=expression)

if __name__ == "__main__":
    app.run(debug=False)
