import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# LOAD DATA
df = pd.read_csv("C:/Users/Asus/Desktop/Diploma/dataset-le.csv")

# FEATURES
X = df[[
    "smoking",
    "alcohol",
    "Obesity",
    "Happiness",
    "GDP",
    "narco",
    "corr",
    "ed",
    "inflation",
    "co2",
    "meat"
]]

# TARGET
y = df["LE_index"]

# MODEL
model = LinearRegression()
model.fit(X, y)

# TITLE
st.title("Life Expectancy Calculator")

# COUNTRY
country = st.selectbox(
    "Select country",
    sorted(df["Country"].unique())
)

# GENDER
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

# SMOKING
smoke = st.selectbox(
    "Smoking",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# ALCOHOL
drink = st.selectbox(
    "Alcohol",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# OBESITY
obesity = st.selectbox(
    "Obesity",
    [0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

# HAPPINESS
happy = st.slider(
    "Happiness Level",
    0.0,
    10.0,
    5.0
)

# BUTTON
if st.button("Predict"):

    # COUNTRY DATA
    row = df[df["Country"] == country].iloc[0]

    # INPUT DATA
    input_data = pd.DataFrame([{
        "smoking": smoke,
        "alcohol": drink,
        "Obesity": obesity,
        "Happiness": happy,
        "GDP": row["GDP"],
        "narco": row["narco"],
        "corr": row["corr"],
        "ed": row["ed"],
        "inflation": row["inflation"],
        "co2": row["co2"],
        "meat": row["meat"]
    }])

    # PREDICTION
    prediction = model.predict(input_data)[0]

    # GENDER EFFECT
    if gender == "Female":
        prediction += 3
    else:
        prediction -= 3

    # REAL VALUE
    real_le = row["LE_index"]

    # RESULTS
    st.success(
        f"Predicted life expectancy: {prediction:.1f} years"
    )

    st.info(
        f"Estimated range: {prediction-3:.1f} - {prediction+3:.1f} years"
    )

    st.write(
        f"Average life expectancy in {country}: {real_le:.1f}"
    )