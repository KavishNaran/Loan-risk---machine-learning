# Bankruptcy Machine Learning Model 

## Table of Contents
- [Project Overview](#project-overview)
- [Code Contributors](#code-contributors)
- [Applications](#applications)
- [File Layout](#file-layout)
- [Sources](#sources)

## Project Overview
Bankruptcy prediction in machine learning involves developing models to forecast the likelihood of financial insolvency for companies or individuals. Analyzing key financial indicators, such as ratios and cash flow, using algorithms like logistic regression or neural networks, enables early detection of potential distress. These models aid lenders, investors, and policymakers in making informed decisions, mitigating economic risks, and maintaining financial stability.

This project uses machine learning to predict whether an individual will become bankrupt based on their financial history. The ensemble model, neural network, and random forest are used to predict the outcome. The selected model is saved in joblib format so it can be used in JavaScript. Users can predict the result by entering values in a local host created by Javascript and jumping to a new webpage with the result.

## Code Contributors

Chang Yu

Damian Kifuso

Kavish Naran 

## Applications

- Python
- Javascript
- CSS
- Tensorflow
- Data Visualization Tools:
- D3.js
- matplotlib (Python)
- Flask


##  File Layout
All links in this section take you directly to the file in the repository.

- [app.py](app.py)
    - This Python script uses the Flask web framework to create a simple web application for bankruptcy prediction. 


### [Jupyter Notebooks](jupyter-notebooks)
- [untitled_project](Tupyter_Notebooks/untitled-project)
    - The folder contains trials result for the neural network model.
- [Data Analysis.ipynb](Jupyter_Notebooks/data-analysis.ipynb)
    - This file creates visualizations for features that may impact bankruptcies.
- [Data Prepration.ipynb](jupyter_notebookss/data-prepration.ipynb)
    - The file contains codes for data cleaning, such as removing unwanted columns, removing null values, standardizing the dataset, and saving it as a database.
- [Ensemble Model.ipynb](jupyter_notebooks/ensemble-model.ipynb)
    - The file contains codes about creating an ensemble model, a machine-learning technique that involves combining the predictions of multiple models to improve overall performance and generalization.
    - Result
      Classification Report
      Accuracy Score: 0.9876
            precision    recall  f1-score   support

           0       1.00      0.99      0.99     20075
           1       0.28      1.00      0.44        96

    accuracy                           0.99     20171
   macro avg       0.64      0.99      0.71     20171
weighted avg       1.00      0.99      0.99     20171

- [Neural Network.ipynb](jupter-notebooks/neural-network.ipynb)
    - The file contains codes about creating a neural network model. Deep learning models inspired by the human brain. They consist of layers of interconnected nodes and are used for complex tasks like image recognition and natural language processing.
    - Result
      Accuracy Score : 0.8884927464961888
      Classification Report
              precision    recall  f1-score   support

           0       0.89      1.00      0.94     14454
           1       0.00      0.00      0.00      1814

    accuracy                           0.89     16268
   macro avg       0.44      0.50      0.47     16268
weighted avg       0.79      0.89      0.84     16268

- [Random Forest Model.ipynb](jupter-notebooks/random-forest-model.ipynb)
    - The file contains codes about creating a random forest model that builds decision trees and merges their predictions, often improving the overall accuracy of the models.
    - Result
      Accuracy Score: 0.9794
      Classification Report
              precision    recall  f1-score   support

           0       1.00      0.98      0.99     17961
           1       0.85      0.98      0.91      2210

    accuracy                           0.98     20171
    macro avg       0.92      0.98      0.95     20171
    weighted avg       0.98      0.98      0.98     20171

### [Resources](Resources)
- [Clean_test_scaled.csv](resources/clean_test_scaled.csv)
    - The file contains the cleaned and scaled data from Credit_test.csv.
- [Clean_train.csv](resources/clean_train.csv)
    - The file contains the cleaned data from Credit_train.csv for data analysis.
- [Clean_train_scaled.csv](resources/clean_train_scaled.csv)
    - The file contains the cleaned and scaled data from Credit_trian.csv.
- [Credit_train.csv](resources/credit_train.csv)
    - The dataset contains information about bank loan status consisting of the following variables: Loan ID, Customer ID, Current Loan Amount, Term, Credit score, Annual income, Years in current job, Homeownership, and bankruptcy for training.
- [clean_train.db](resources/clean_train.db)
    - This database is saved from clean_train_scaled.csv for further coding.
- [credit_test.csv](resources/credit_test.csv)
    - The dataset contains information about bank loan status consisting of the following variables: Loan ID, Customer ID, Current Loan Amount, Term, Credit score, Annual income, Years in current job, Homeownership, and bankruptcy for testing.
- [random_forest_model.joblib](resources/random_forest_model.joblib)
  - This file contains codes saved from the random forest model.
    
### [templates](templates)
- [index.html](templates/index.html)
  - This file contains JavaScript codes for the user input form.
- [result.html](templates/result.html)
  - This file contains JavaScript codes for the user result.
    
## Sources
### Data: https://www.kaggle.com/datasets/zaurbegiev/my-dataset
          https://www.hackersrealm.net/post/loan-prediction-analysis-using-python                 
          https://www.irjmets.com/uploadedfiles/paper/volume3/issue_1_january_2021/5540/1628083223.pdf
        
