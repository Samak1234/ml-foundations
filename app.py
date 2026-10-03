import streamlit as st

st.title("Used Car Price Estimator")

st.write(
    "Estimate the resale value of a used car using a machine learning model."
)

st.divider()

present_price = st.number_input(
    "Present Price (in lakh)",
    min_value=0.0,
    step=0.1
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    step=1000
)

car_age = st.number_input(
    "Car Age",
    min_value=0,
    step=1
)

owners = st.number_input(
    "Previous Owners",
    min_value=0,
    step=1
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

predict_button = st.button("Predict Price")

if predict_button:
    st.success("Form submitted successfully.")