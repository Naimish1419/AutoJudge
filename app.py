from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

classifier = joblib.load("classifier.pkl")
regressor = joblib.load("regressor.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        description = request.form["description"]
        input_desc = request.form["input_description"]
        output_desc = request.form["output_description"]

        text = description + " " + input_desc + " " + output_desc

        pred_class = classifier.predict([text])[0]
        pred_score = np.expm1(regressor.predict([text])[0])

        return render_template(
            "index.html",
            pred_class=pred_class,
            pred_score=round(pred_score, 2)
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

