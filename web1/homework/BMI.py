from flask import Flask,render_template
app = Flask(__name__)
@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
    BMI = w/(h/100*h/100)
    if BMI < 16:
        return ("BMI: " + str(BMI) + "  Severely Underweight")
    elif 16 <= BMI < 18.5:
        return ("BMI: " + str(BMI) + "  Underweight")
    elif 18.5 <= BMI < 25:
        return ("BMI: " + str(BMI) + "  Normal")
    elif 25 <= BMI < 30:
        return ("BMI: " + str(BMI) + "  Overweight")
    else:
        return ("BMI: " + str(BMI) + "  Obese")
if __name__ == '__main__':
    app.run(debug=True)