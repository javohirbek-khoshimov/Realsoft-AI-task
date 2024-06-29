# Realsoft-AI-task

# Dataset Prediction

This project aims to predict datasets based on various features. The dataset and preprocessing steps, as well as the training of different models, are included in this notebook.

## Table of Contents
- [Dataset](#dataset)
- [Data Preprocessing](#data-preprocessing)
- [Models](#models)
- [Evaluation](#evaluation)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset
The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com). It contains various datasets related to any field.

## Data Preprocessing
1. **Loading Data:** The data is loaded using pandas.
2. **Data Cleaning:** Handling missing values, encoding categorical variables, and feature scaling.
3. **Feature Selection:** Selecting relevant features for the prediction task.

## Models
Various machine learning models are trained and evaluated:
1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**

## Evaluation
The models are evaluated using:
- R² Score
- Mean Squared Error (MSE)

## Results
The Decision Tree Regressor provided the best results with the following metrics:
- **R² Score:** 0.25
- **Mean Squared Error:** 158.17

## Usage
To run the notebook, follow these steps:
1. Clone the repository.
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Jupyter Notebook:
    ```bash
    jupyter notebook Stedent-Performance.ipynb
    ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
