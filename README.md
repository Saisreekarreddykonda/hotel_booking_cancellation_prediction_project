# 🏨 Hotel Booking Cancellation Prediction

## 🚀 Project Overview

This project aims to predict hotel booking cancellations using historical booking data. It was developed as part of an internship project under the guidance of **Trendalytix**. The system leverages data preprocessing, exploratory data analysis (EDA), and machine learning techniques to forecast whether a booking will be canceled or not.

🎯 **Objective**: Assist hotel management in reducing cancellations, optimizing bookings, and improving strategic decisions using a predictive ML pipeline and an interactive Power BI dashboard.

---

## 🤝 Team Details

**Project Type:** Internship-based Team Project

**Team Leader:** [Varshini Chilakala](https://github.com/Varshini-Chilakala)

**Team Member 1:** [Sai Sreekar Reddy Konda](https://github.com/Saisreekarreddykonda)

**Team Member 2:** Diti Solanki

**Organization:** Trendalytix

**Tools Used:** Python, Pandas, Scikit-learn, XGBoost, Power BI, Jupyter Notebook

---

## 🗅️ Problem Statement

Booking cancellations can lead to significant revenue loss and poor capacity planning for hotels. The goal of this project is to predict which bookings are likely to be canceled, using features like:

* Lead time
* Customer type
* Deposit type
* Booking changes, etc.

---

## 📊 Dataset

* **Source:** [Kaggle – Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
* **File:** `hotel_bookings.csv`
* **Size:** \~32 features, 119,000+ rows
* **Cleaned Version:** `cleaned_hotel_bookings_data.csv`

---

## 📁 Folder Structure

```
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
│   ├── univariate_analysis/
│   └── bivariate_analysis/
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
```

---

## ⚙️ Project Workflow

### 1. 🧼 Data Cleaning & Preprocessing

* Removed duplicates and handled missing values (`company`, `agent`, `children`, `country`)
* Capped outliers in `lead_time`, `adr`, and `previous_cancellations`
* Feature engineering:

  * `total_stay`, `total_guests`, `room_mismatch`, `is_family`, `is_repeated_customer`
* Merged date-related columns into a unified `arrival_date`

---

### 2. 📊 Exploratory Data Analysis (EDA)

* **Univariate Analysis:**

  * Cancellation distribution
  * Hotel type frequency
  * Distribution of `lead_time`, `meal`, `market_segment`, etc.

* **Bivariate Analysis:**

  * Cancellation rates by:

    * Hotel type
    * Deposit type
    * Customer type
    * Month and year (seasonal trends)
    * Country
    * Lead time
    * Market segment

---

### 3. 🧠 Feature Engineering

* One-hot encoded all relevant categorical features
* Removed date and ID-like columns (`reservation_status_date`, `arrival_date_year`, etc.)
* Scaled/standardized features as needed
* Final feature set: \~60 engineered predictors

---

### 4. 🤖 Model Development

#### Algorithms Tested:

* ✅ **XGBoost (Best Model)**
* Random Forest
* Logistic Regression
* Decision Tree

#### Final XGBoost Model Results:

* **Accuracy:** 84%
* **Precision (Canceled):** 0.74
* **Recall (Canceled):** 0.67
* **F1-Score (Canceled):** 0.71

#### 📈 Model Performance Comparison

| Model               | Accuracy | Precision (Canceled) | Recall (Canceled) | F1-Score (Canceled) |
| ------------------- | -------- | -------------------- | ----------------- | ------------------- |
| Random Forest       | 84%      | 0.74                 | 0.67              | 0.70                |
| Logistic Regression | 74%      | 0.53                 | 0.79              | 0.63                |
| **XGBoost (Best)**  | 84%      | 0.74                 | 0.67              | 0.71                |
| Decision Tree       | 70%      | 0.48                 | 0.89              | 0.62                |

---

### 5. 📊 Dashboard Development (Power BI)

* Built dynamic KPIs and slicers to filter data by:

  * Booking year, country, month
  * Deposit type, hotel type, and customer type
* Key visual insights:

  * Cancellations vs. country
  * Parking requests and cancellation relationship
  * Lead time patterns
  * ADR and revenue implications

---

### 6. 📦 Final Deliverables

* 📄 **Project Report** (PDF)
* 🔧 **Trained ML Model** (`xgboost_cancellation_model.pkl`)
* 📊 **Interactive Dashboard** (Power BI)
* 🔬 **Prediction Pipeline Script** (`hotel_booking_pipeline.py`)

---

## 🔄 How to Use This Project

### ⚙️ Setup Environment

```bash
pip install -r requirements.txt
```

### 🧪 Predict on New Data

```bash
python hotel_booking_pipeline.py
```

### 📒 Explore in Jupyter Notebook

Open:

```
notebooks/Hotel_bookings.ipynb
```

---

## 📚 Key Learnings

* Real-world data issues: missing values, skewed distributions, class imbalance
* Feature engineering and its impact on model performance
* Importance of EDA in uncovering hidden insights
* Deployable scripts and dashboard integration for business use

---

## 💼 Contact

Varshini Chilakala

📧 Email: [varshini.chilakala27@gmail.com](mailto:varshini.chilakala27@gmail.com)

🐙 GitHub: [@Varshini-Chilakala](https://github.com/Varshini-Chilakala)

---

## 🚩 Acknowledgment

Thanks to **Trendalytix** and our mentors for their support and valuable guidance during this internship project.
