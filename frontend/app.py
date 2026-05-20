import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

st.title("Customer Churn Prediction System")

st.write("Predict customer churn and generate recommendations")


# INPUT FORM

Age = st.number_input("Age", 18, 100, 35)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Country = st.text_input(
    "Country",
    "India"
)

Membership_Years = st.slider(
    "Membership Years",
    0.0,
    10.0,
    3.0
)

Login_Frequency = st.slider(
    "Login Frequency",
    0.0,
    50.0,
    15.0
)

Session_Duration_Avg = st.slider(
    "Session Duration Avg",
    0.0,
    100.0,
    25.0
)

Pages_Per_Session = st.slider(
    "Pages Per Session",
    0.0,
    30.0,
    7.0
)

Cart_Abandonment_Rate = st.slider(
    "Cart Abandonment Rate",
    0.0,
    100.0,
    20.0
)

Wishlist_Items = st.slider(
    "Wishlist Items",
    0,
    20,
    4
)

Total_Purchases = st.slider(
    "Total Purchases",
    0,
    100,
    12
)

Average_Order_Value = st.number_input(
    "Average Order Value",
    0,
    100000,
    5000
)

Days_Since_Last_Purchase = st.slider(
    "Days Since Last Purchase",
    0,
    365,
    8
)

Discount_Usage_Rate = st.slider(
    "Discount Usage Rate",
    0.0,
    100.0,
    25.0
)

Returns_Rate = st.slider(
    "Returns Rate",
    0.0,
    100.0,
    5.0
)

Email_Open_Rate = st.slider(
    "Email Open Rate",
    0.0,
    100.0,
    60.0
)

Customer_Service_Calls = st.slider(
    "Customer Service Calls",
    0,
    20,
    1
)

Product_Reviews_Written = st.slider(
    "Product Reviews Written",
    0,
    50,
    3
)

Social_Media_Engagement_Score = st.slider(
    "Social Media Engagement Score",
    0.0,
    100.0,
    50.0
)

Mobile_App_Usage = st.slider(
    "Mobile App Usage",
    0.0,
    100.0,
    70.0
)

Payment_Method_Diversity = st.slider(
    "Payment Method Diversity",
    0.0,
    10.0,
    3.0
)

Lifetime_Value = st.number_input(
    "Lifetime Value",
    0,
    1000000,
    150000
)

Credit_Balance = st.number_input(
    "Credit Balance",
    0,
    100000,
    2000
)

Signup_Quarter = st.selectbox(
    "Signup Quarter",
    ["Q1", "Q2", "Q3", "Q4"]
)

# PREDICT BUTTON

if st.button("Predict"):

    data = {

        "Age": Age,
        "Gender": Gender,
        "Country": Country,
        "Membership_Years": Membership_Years,
        "Login_Frequency": Login_Frequency,
        "Session_Duration_Avg": Session_Duration_Avg,
        "Pages_Per_Session": Pages_Per_Session,
        "Cart_Abandonment_Rate": Cart_Abandonment_Rate,
        "Wishlist_Items": Wishlist_Items,
        "Total_Purchases": Total_Purchases,
        "Average_Order_Value": Average_Order_Value,
        "Days_Since_Last_Purchase": Days_Since_Last_Purchase,
        "Discount_Usage_Rate": Discount_Usage_Rate,
        "Returns_Rate": Returns_Rate,
        "Email_Open_Rate": Email_Open_Rate,
        "Customer_Service_Calls": Customer_Service_Calls,
        "Product_Reviews_Written": Product_Reviews_Written,
        "Social_Media_Engagement_Score": Social_Media_Engagement_Score,
        "Mobile_App_Usage": Mobile_App_Usage,
        "Payment_Method_Diversity": Payment_Method_Diversity,
        "Lifetime_Value": Lifetime_Value,
        "Credit_Balance": Credit_Balance,
        "Signup_Quarter": Signup_Quarter
    }

    response = requests.post(
        "https://customer-churn-api-7nqw.onrender.com/predict",
        json=data
    )

    result = response.json()

    st.success("Prediction Completed")

    st.subheader("Prediction")

    st.write(result["prediction"])

    st.subheader("Churn Probability")

    st.write(result["churn_probability"])

    st.subheader("Customer Segment")

    st.write(result["customer_segment"])

    st.subheader("Recommendations")

    for rec in result["recommendations"]:

        st.write("•", rec)