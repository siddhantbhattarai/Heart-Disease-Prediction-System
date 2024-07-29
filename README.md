# Heart Disease Prediction System

![Screenshot 1](test-cases/Screenshot%20from%202024-07-29%2016-51-37.png)
![Screenshot 2](test-cases/Screenshot%20from%202024-07-29%2016-51-45.png)

## Overview
The Heart Disease Prediction System is a machine learning project designed to predict the risk of heart disease based on various health and lifestyle factors. This project aims to provide a helpful tool for early detection and prevention of heart disease, supporting healthcare professionals in making better clinical decisions.

## Features
- Predicts the risk of heart disease based on user inputs.
- Utilizes a machine learning model trained on a comprehensive dataset of health records.
- User-friendly interface for healthcare professionals and patients.
- Offers visualizations to demonstrate the influence of different factors on heart disease risk.

## Dataset
The dataset used for training the model includes various health metrics and demographic information. The features include:
- `age`
- `sex`
- `cp` (chest pain type)
- `trestbps` (resting blood pressure)
- `chol` (serum cholesterol in mg/dl)
- `fbs` (fasting blood sugar > 120 mg/dl)
- `restecg` (resting electrocardiographic results)
- `thalach` (maximum heart rate achieved)
- `exang` (exercise induced angina)
- `oldpeak` (ST depression induced by exercise relative to rest)
- `slope` (the slope of the peak exercise ST segment)
- `ca` (number of major vessels colored by fluoroscopy)
- `thal` (thalassemia)

The target variable is `heart_disease`.

## Installation
To run the Heart Disease Prediction System locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/siddhantbhattarai/heart-disease-prediction-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd heart-disease-prediction-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```bash
    python app.py
    ```

## Usage
- Open a web browser and go to `http://127.0.0.1:5000/`.
- Enter the required information in the input fields.
- Click on the "Predict" button to get the heart disease risk prediction.
- View the results and visualizations.

## Model
The prediction model is built using a Support Vector Machine (SVM) algorithm. The model file `svm_model.pkl` is stored in the `models` directory.

## Screenshots
![Screenshot 1](test-cases/Screenshot%20from%202024-07-29%2016-51-37.png)
![Screenshot 2](test-cases/Screenshot%20from%202024-07-29%2016-51-45.png)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


