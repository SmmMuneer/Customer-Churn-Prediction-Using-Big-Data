from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the XGBoost model
with open('xgboost_model.pkl', 'rb') as file:
    xgboost_model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Render the input form

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    data = request.form
    try:
        # Extract input features
        features = [
            int(data['Gender']),
            int(data['Tenure']),
            float(data['Usage Frequency']),
            int(data['Support Calls']),
            int(data['Payment Delay']),
            int(data['Subscription Type']),
            int(data['Contract Length']),
            float(data['Total Spend']),
            int(data['Last Interaction'])
        ]
        
        # Convert to numpy array
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = xgboost_model.predict(features_array)[0]
        
        # Redirect to the appropriate page
        if prediction == 1:
            return render_template('churn.html')  # Churn page
        else:
            return render_template('not_churn.html')  # Not Churn page
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
