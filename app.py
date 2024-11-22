from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load(r"C:/Users/ASUS/OneDrive - Lambton College/Documents/drought_prediction_model.pkl")

@app.route("/")
def home():
    # Render the template with empty input values initially
    return render_template("index.html", values={}, prediction_text="")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            # Extract input features from the form
            soil_quality3 = float(request.form["soil_quality3"])  # SQ3
            soil_quality2 = float(request.form["soil_quality2"])  # SQ2
            grassland = float(request.form["grassland"])          # GRS_LAND
            soil_quality6 = float(request.form["soil_quality6"])  # SQ6
            soil_quality4 = float(request.form["soil_quality4"])  # SQ4

            # Prepare the features array
            features = np.array([[soil_quality3, soil_quality2, grassland, soil_quality6, soil_quality4]])

            # Make prediction
            prediction = model.predict(features)

            # Store the entered values to pass back to the template
            values = {
                "soil_quality3": soil_quality3,
                "soil_quality2": soil_quality2,
                "grassland": grassland,
                "soil_quality6": soil_quality6,
                "soil_quality4": soil_quality4,
            }

            # Return prediction result along with entered values
            prediction_text = f"Drought Level: {int(prediction[0])}"
            return render_template("index.html", prediction_text=prediction_text, values=values)
        except Exception as e:
            # Return error message along with entered values
            values = request.form
            return render_template("index.html", prediction_text=f"Error: {str(e)}", values=values)

if __name__ == "__main__":
    app.run(debug=True)
