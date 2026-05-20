# Customer Churn Prediction & Recommendation System

## Project Overview

This project predicts whether a customer is likely to churn and generates personalized recommendations based on customer behavior and segmentation.

The system uses Machine Learning for churn prediction and KMeans clustering for customer segmentation. A FastAPI backend serves predictions, and a Streamlit frontend provides an interactive user interface.

---

## Features

✔ Customer churn prediction

✔ Churn probability score

✔ Customer segmentation using KMeans

✔ Recommendation engine

✔ Feature engineering

✔ FastAPI REST API

✔ Interactive Streamlit UI

✔ Swagger API documentation

✔ Saved ML models using Joblib

✔ Ready for cloud deployment

---

## Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Joblib
- Requests

### Backend

- FastAPI
- Uvicorn

### Frontend

- Streamlit

### ML Algorithms

- Random Forest Classifier
- KMeans Clustering

---

## Dataset Features

The dataset includes customer behavioral features:

- Age
- Gender
- Country
- Membership_Years
- Login_Frequency
- Session_Duration_Avg
- Pages_Per_Session
- Cart_Abandonment_Rate
- Wishlist_Items
- Total_Purchases
- Average_Order_Value
- Days_Since_Last_Purchase
- Discount_Usage_Rate
- Returns_Rate
- Email_Open_Rate
- Customer_Service_Calls
- Product_Reviews_Written
- Social_Media_Engagement_Score
- Mobile_App_Usage
- Payment_Method_Diversity
- Lifetime_Value
- Credit_Balance
- Signup_Quarter

Target Variable:

- Churned

---

## Feature Engineering

Custom features created:

### Engagement Score

```python
Engagement_score = (
Login_Frequency +
Pages_Per_Session +
Session_Duration_Avg
)
```

### Purchase Power

```python
Purchase_Power =
Total_Purchases * Average_Order_Value
```

### Recency Score

```python
Recency_Score =
1/(Days_Since_Last_Purchase+1)
```

### Discount Sensitivity

```python
Discount_sensitivity =
Discount_Usage_Rate * Total_Purchases
```

### Activity Ratio

```python
Activity_Ratio =
Login_Frequency/(Membership_Years+1)
```

### Customer Value

```python
Customer_Value =
Lifetime_Value/(Total_Purchases+1)
```

### Engagement Per Purchase

```python
Engagement_Per_Purchase =
Engagement_score/(Total_Purchases+1)
```

---

## Machine Learning Workflow

### Data Preprocessing

- Missing value handling
- Encoding categorical variables
- Standard scaling
- Train test split

### Model Training

Random Forest Classifier

### Customer Segmentation

KMeans clustering:

Cluster 0 → High Engagement Users

Cluster 1 → Moderate Users

Cluster 2 → Low Activity Users

Cluster 3 → Inactive Users

---

## Project Structure

```text
Customer-Churn-Project/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── app.py
│
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   ├── imputer.pkl
│   ├── feature_columns.pkl
│   ├── kmeans_model.pkl
│   ├── cluster_scaler.pkl
│   └── cluster_features.pkl
│
├── notebook/
│   └── customer_churn.ipynb
│
├── data/
│   └── ecommerce_customer_churn_dataset.csv
│
├── requirements.txt
│
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/customer-churn-project.git

cd customer-churn-project
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Backend

Move to backend folder:

```bash
cd backend
```

Start FastAPI:

```bash
uvicorn app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

Move to frontend folder:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

Frontend:

```text
http://localhost:8501
```

---

## API Endpoint

### POST

```text
/predict
```

Input Example:

```json
{
"Age":35,
"Gender":"Male",
"Country":"India",
"Membership_Years":3,
"Login_Frequency":15,
"Session_Duration_Avg":25,
"Pages_Per_Session":7,
"Cart_Abandonment_Rate":20,
"Wishlist_Items":4,
"Total_Purchases":12,
"Average_Order_Value":5000,
"Days_Since_Last_Purchase":8,
"Discount_Usage_Rate":25,
"Returns_Rate":5,
"Email_Open_Rate":60,
"Customer_Service_Calls":1,
"Product_Reviews_Written":3,
"Social_Media_Engagement_Score":50,
"Mobile_App_Usage":70,
"Payment_Method_Diversity":3,
"Lifetime_Value":150000,
"Credit_Balance":2000,
"Signup_Quarter":"Q2"
}
```

Response Example:

```json
{
"prediction":"Not Churn",
"churn_probability":0.24,
"cluster":0,
"customer_segment":"High Engagement Users",
"recommendations":[
"VIP rewards",
"Premium membership",
"Exclusive deals"
]
}
```

---

## Future Improvements

- Deep learning model implementation
- Real-time customer tracking
- Database integration
- Authentication system
- Dashboard analytics
- Email notification system

---

## Author

Yogesh Baranwal

Machine Learning | Data Science | Python | FastAPI | Streamlit