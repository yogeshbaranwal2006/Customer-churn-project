from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"


# LOAD MODELS


rf = joblib.load(MODEL_DIR / "churn_model (1).pkl")

scaler = joblib.load(MODEL_DIR / "scaler (1).pkl")

feature_columns = joblib.load(
    MODEL_DIR / "feature_columns (1).pkl"
)

kmeans = joblib.load(
    MODEL_DIR / "kmeans_model (1).pkl"
)

cluster_scaler = joblib.load(
    MODEL_DIR / "cluster_scaler (1).pkl"
)

cluster_features = joblib.load(
    MODEL_DIR / "cluster_features (1).pkl"
)


# FASTAPI


app = FastAPI()


# INPUT SCHEMA


class CustomerData(BaseModel):

    Age: int
    Gender: str
    Country: str
    Membership_Years: float
    Login_Frequency: float
    Session_Duration_Avg: float
    Pages_Per_Session: float
    Cart_Abandonment_Rate: float
    Wishlist_Items: float
    Total_Purchases: float
    Average_Order_Value: float
    Days_Since_Last_Purchase: float
    Discount_Usage_Rate: float
    Returns_Rate: float
    Email_Open_Rate: float
    Customer_Service_Calls: float
    Product_Reviews_Written: float
    Social_Media_Engagement_Score: float
    Mobile_App_Usage: float
    Payment_Method_Diversity: float
    Lifetime_Value: float
    Credit_Balance: float
    Signup_Quarter: str


# HOME ROUTE


@app.get("/")
def home():

    return {
        "message": "Customer Churn API Running"
    }


# PREDICTION ROUTE


@app.post("/predict")
def predict(customer: CustomerData):

    # Convert input into dataframe
    customer_df = pd.DataFrame([customer.dict()])


    # FEATURE ENGINEERING
   

    customer_df['Engagement_score'] = (
        customer_df['Login_Frequency']
        + customer_df['Pages_Per_Session']
        + customer_df['Session_Duration_Avg']
    )

    customer_df['Purchase_Power'] = (
        customer_df['Total_Purchases']
        * customer_df['Average_Order_Value']
    )

    customer_df['Recency_Score'] = (
        1 / (customer_df['Days_Since_Last_Purchase'] + 1)
    )

    customer_df['Discount_sensitivity'] = (
        customer_df['Discount_Usage_Rate']
        * customer_df['Total_Purchases']
    )

    customer_df['Activity_Ratio'] = (
        customer_df['Login_Frequency']
        / (customer_df['Membership_Years'] + 1)
    )

    customer_df['Customer_Value'] = (
        customer_df['Lifetime_Value']
        / (customer_df['Total_Purchases'] + 1)
    )

    customer_df['Engagement_Per_Purchase'] = (
        customer_df['Engagement_score']
        / (customer_df['Total_Purchases'] + 1)
    )

    
    # CLUSTER DATAFRAME
    

    cluster_df = customer_df[cluster_features]

    
    # ENCODING
    

    customer_df = pd.get_dummies(customer_df)

   
    # MATCH TRAINING COLUMNS
    

    customer_df = customer_df.reindex(
        columns=feature_columns,
        fill_value=0
    )

  
    # SCALING
    

    customer_df = scaler.transform(customer_df)

   
    # CHURN PREDICTION
    

    churn_probability = rf.predict_proba(
        customer_df
    )[:,1][0]

    prediction = (
        "Churn"
        if churn_probability > 0.3
        else "Not Churn"
    )

   
    # CLUSTER PREDICTION
   

    cluster_scaled = cluster_scaler.transform(
        cluster_df
    )

    cluster = int(
        kmeans.predict(cluster_scaled)[0]
    )

    
    # RECOMMENDATION ENGINE
   

    recommendations = []

    if cluster == 0:

        segment = "High Engagement Users"

        recommendations.extend([
            "VIP rewards",
            "Premium membership",
            "Exclusive deals"
        ])

    elif cluster == 1:

        segment = "Moderate Users"

        recommendations.extend([
            "Email campaigns",
            "Product recommendations"
        ])

    elif cluster == 2:

        segment = "Low Activity Users"

        recommendations.extend([
            "Discount coupons",
            "Retention campaigns"
        ])

    else:

        segment = "Inactive Users"

        recommendations.extend([
            "Push notifications",
            "Reactivation offers"
        ])

   
    # FINAL RESPONSE
  

    return {

        "prediction": prediction,

        "churn_probability": round(
            float(churn_probability),
            2
        ),

        "cluster": cluster,

        "customer_segment": segment,

        "recommendations": recommendations
    }