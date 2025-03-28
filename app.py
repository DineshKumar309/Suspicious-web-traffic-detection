from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Decision Tree model
model_filename = "decision_tree_model.pkl"
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get input values from the form
        feature_1 = float(request.form['feature_1'])
        feature_2 = float(request.form['feature_2'])
        feature_3 = float(request.form['feature_3'])
        feature_4 = float(request.form['feature_4'])
        
        # Convert inputs to NumPy array
        input_features = np.array([[feature_1, feature_2, feature_3, feature_4]])

        # Predict using the model
        prediction = model.predict(input_features)
        
        # Convert prediction to a readable output
        result = "🚨 Suspicious Traffic" if prediction[0] == 1 else "✅ Normal Traffic"
        
        return render_template('index.html', prediction=result)

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)