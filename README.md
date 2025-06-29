Hotel Booking Cancellation Prediction

🚀 Project Overview

This project aims to predict hotel booking cancellations using historical booking data. It was developed as part of an internship project under the guidance of Trendalytix. The system leverages data preprocessing, exploratory data analysis (EDA), and machine learning techniques to forecast whether a booking will be canceled or not.

The ultimate goal is to assist hotel management in reducing cancellations, optimizing bookings, and improving business decisions using a predictive pipeline and dashboard.


🤝 Team Details

Project Type: Internship-based Team Project

Team Leader: [Varshini Chilakala](https://github.com/Varshini-Chilakala)

Team Member 1: [Sai Sreekar Reddy Konda](https://github.com/Saisreekarreddykonda)

Team Member 2: [Diti Solanki]

Organization: Trendalytix

Tools Used: Python, Pandas, Scikit-learn, XGBoost, Power BI, Jupyter Notebook


🗅️ Problem Statement

Booking cancellations impact hotel revenue and occupancy planning. The goal is to identify bookings that are more likely to be canceled based on features such as lead time, customer type, deposit type, and more.


📊 Dataset

Source: Kaggle / Public Hotel Booking Dataset

https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

File: hotel_bookings.csv

Size: ~32 features, 119,000+ rows

Cleaned Dataset: cleaned_hotel_bookings_data.csv



📁 Folder Structure

hotel_booking_cancellation_prediction_project/
│
├── data/
│   ├── hotel_bookings.csv
│   └── cleaned_hotel_bookings_data.csv
│
├── notebooks/
│   └── Hotel_bookings.ipynb
│
├── models/
│   └── xgboost_cancellation_model.pkl
│
├── plots/
│   └── univariate_analysis
│   └── bivariate_analysis
│
├── dashboard/
│   └── cancellation_dashboard.jpg
│
├── report/
│   └── Hotel_Booking_Cancellation_Prediction_Report.pdf
│
├── hotel_booking_pipeline.py
├── README.md
├── requirements.txt


⚙️ Project Workflow

1. Data Cleaning & Preprocessing

Removed duplicates and handled missing values

Filled company, agent, children, country intelligently

Capped extreme outliers in lead_time, adr, and previous_cancellations

Created new features:

total_stay, total_guests, room_mismatch, is_family, is_repeated_customer

Converted dates into a single arrival_date


2. Exploratory Data Analysis (EDA)

Univariate: Distributions of cancellations, hotel types, meals, customer types

Bivariate: Cancellation rates by year, month, deposit type, car parking


3. Feature Engineering

One-hot encoded all relevant categorical features

Dropped ID-like and date decomposition columns

Scaled numerical fields (if needed)


4. Model Development

Algorithms used:

Random Forest

Logistic Regression

XGBoost ✅ (Best)

Decision Tree

Final XGBoost Model Results:

Accuracy: 84%

Precision (Canceled): 0.74

Recall (Canceled): 0.67

F1-score (Canceled): 0.71

### 📈 Model Performance Comparison

| Model               | Accuracy | Precision (Canceled) | Recall (Canceled) | F1-Score (Canceled) |
|---------------------|----------|-----------------------|--------------------|----------------------|
| Random Forest        | 84%      | 0.74                  | 0.67               | 0.70                 |
| Logistic Regression  | 74%      | 0.53                  | 0.79               | 0.63                 |
| XGBoost (Best Model) | 84%      | 0.74                  | 0.67               | 0.71                 |
| Decision Tree        | 70%      | 0.48                  | 0.89               | 0.62                 |


5. Dashboard Development (Power BI)

Created KPIs for cancellations by year, country, month

Tracked total bookings, customer type mix, ADR patterns

Visual insights on lead time and parking space effects

Included slicers, stacked bars, and interactive visual filters


6. Final Deliverables

📄 Detailed project report

🔧 Trained ML model (.pkl)

📊 Dashboard visual in Power BI

🔬 Predictive Python script for inference



🔄 How to Use This Project

Setup Environment

pip install -r requirements.txt


Predict on New Data

python hotel_booking_pipeline.py


Jupyter Notebook Exploration

Open the full workflow:

notebooks/Hotel_bookings.ipynb


Key Learnings

Importance of feature engineering and EDA

Handling real-world data: imbalances, outliers, missing values

Deployment-readiness of models using joblib and scripting

Dashboard creation with business relevance


💼 Contact

For any queries related to the project:Varshini Chilakala
Email: [varshini.chilakala27@gmail.com]
GitHub: [Varshini-Chilakala](https://github.com/Varshini-Chilakala)


🚩 Acknowledgment

Thanks to Trendalytix and mentors for their guidance during this internship project.
