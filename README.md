# Realsoft-AI-task

Student Performance Prediction
This project aims to predict student performance based on various features. The dataset and preprocessing steps, as well as the training of different models, are included in this notebook.

Table of Contents
Dataset
Data Preprocessing
Models
Evaluation
Results
Usage
Contributing
License
Dataset
The dataset used in this project is sourced from Kaggle. It contains various features related to student demographics, study time, and previous scores.

Data Preprocessing
Loading Data: The data is loaded using pandas.
Data Cleaning: Handling missing values, encoding categorical variables, and feature scaling.
Feature Selection: Selecting relevant features for the prediction task.
Models
Various machine learning models are trained and evaluated:

Linear Regression
Decision Tree Regressor
Random Forest Regressor
Evaluation
The models are evaluated using:

R² Score
Mean Squared Error (MSE)
Results
The Decision Tree Regressor provided the best results with the following metrics:

R² Score: 0.25
Mean Squared Error: 158.17
Usage
To run the notebook, follow these steps:

Clone the repository.
Install the necessary dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Jupyter Notebook:
bash
Copy code
jupyter notebook Stedent-Performance.ipynb
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.
