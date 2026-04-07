from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)

# ✅ Load the NEW 5-feature trained model
with open("../models/fake_profile_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # ✅ READ ONLY THE 5 FEATURES (MUST MATCH TRAINING ORDER)
        followers_count = float(data['followers_count'])
        friends_count = float(data['friends_count'])
        verified = int(data['verified'])
        default_profile = int(data['default_profile'])
        ff_ratio = float(data['ff_ratio'])

        # ✅ CREATE INPUT ARRAY (ORDER IS VERY IMPORTANT)
        features = np.array([[
            followers_count,
            friends_count,
            verified,
            default_profile,
            ff_ratio
        ]])

        prediction = model.predict(features)[0]

        result = "REAL USER" if prediction == 1 else "FAKE USER"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
