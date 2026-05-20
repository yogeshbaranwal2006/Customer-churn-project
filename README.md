# Customer Churn Prediction & Recommendation System

## Project Overview

This project predicts whether a customer is likely to churn and generates personalized recommendations using customer behavior and segmentation techniques.

The system combines:

- Customer churn prediction using Random Forest
- Customer segmentation using KMeans clustering
- Recommendation generation based on customer segments
- FastAPI backend for prediction APIs
- Streamlit frontend for interactive UI

---

## Features

1. Customer churn prediction  
2. Churn probability score  
3. Customer segmentation using KMeans  
4. Recommendation engine  
5. Feature engineering pipeline  
6. FastAPI REST API  
7. Interactive Streamlit UI  
8. Swagger API documentation  
9. Saved ML models using Joblib  
10. Ready for deployment

---

## Project Structure

```text
Customer-Churn-Project/
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── models/
│   ├── churn_model.pkl
│   ├── cluster_scaler.pkl
│   ├── cluster_features.pkl
│   ├── feature_columns.pkl
│   ├── imputer.pkl
│   └── kmeans_model.pkl
│
├── notebook/
│   └── customer_churn.ipynb
│
├── data/
│   └── ecommerce_customer_dataset.xlsx
│
└── README.md
```

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

Customer data includes:

- Age
- Gender
- Country
- Membership Years
- Login Frequency
- Session Duration Avg
- Pages Per Session
- Cart Abandonment Rate
- Wishlist Items
- Total Purchases
- Average Order Value
- Days Since Last Purchase
- Discount Usage Rate
- Returns Rate
- Email Open Rate
- Customer Service Calls
- Product Reviews Written
- Social Media Engagement Score
- Mobile App Usage
- Payment Method Diversity
- Lifetime Value
- Credit Balance
- Signup Quarter

---

## API Run

Backend:

```bash
cd backend
uvicorn app:app --reload
```

Frontend:

```bash
cd frontend
streamlit run app.py
```

---

## Model Output

Example output:

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

- User authentication
- Database integration
- Docker deployment
- Real-time monitoring
- Advanced recommendation engine

