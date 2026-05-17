import streamlit as st
import base64
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import time
import os

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_local(image_file):
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call with your local file path
set_bg_local('background.png')
# app.py
# 🚀 Sales Revenue AI - CEO Level Premium Version
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Sales Revenue AI",
    page_icon="📈",
    layout="wide"
)

# ---------------- SAFE FILE CHECK ----------------
if not os.path.exists("sales_model.pkl"):
    st.error("sales_model.pkl not found")
    st.stop()

if not os.path.exists("training_columns.pkl"):
    st.error("training_columns.pkl not found")
    st.stop()

# ---------------- LOAD MODEL ----------------
model = joblib.load("sales_model.pkl")
training_columns = joblib.load("training_columns.pkl")


# ---------------- HEADER ----------------
st.markdown("""
<div style="text-align:center; animation: fadeIn 1s;">

<h1>📈 Sales Revenue Predictions Using AI</h1>

<h3>Business Revenue Intelligence Platform</h3>

<p>
Predict future sales revenue using Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SIDEBAR ----------------
if os.path.exists("screen-photo.jpg"):
    st.sidebar.image(
        "screen-photo.jpg",
        use_container_width=True
    )
else:
    st.sidebar.markdown(
        "## 📈 Sales Revenue AI"
    )

st.sidebar.markdown(
    "### AI Business Dashboard"
)

st.sidebar.caption(
    "Built with Python + Machine Learning"
    'Simle Linear Regression project using Scikitlearn'
)
st.sidebar.markdown('Admin Sales Chart Illustrations')
st.sidebar.image('salesprojections.jpg')
st.sidebar.markdown('Created by UpdateCodesML')
# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:

    advertising_budget = st.slider(
        "Advertising Budget (₦)",
        50000,
        2000000,
        500000
    )

    employees = st.slider(
        "Employees",
        1,
        50,
        10
    )

    store_size = st.slider(
        "Store Size",
        200,
        5000,
        1500
    )

with col2:

    customer_visits = st.slider(
        "Customer Visits",
        100,
        10000,
        3000
    )

    product_price = st.slider(
        "Product Price (₦)",
        1000,
        100000,
        12000
    )

    location_score = st.slider(
        "Location Score",
        1,
        10,
        7
    )

season = st.selectbox(
    "Season",
    ["Low","Medium","High"]
)

# ---------------- PREDICT BUTTON ----------------
if st.button("🚀 Predict Revenue"):

    try:

        # ---------------- CREATE DATAFRAME ----------------
        new_data = pd.DataFrame({

            "Advertising_Budget":[advertising_budget],

            "Employees":[employees],

            "Store_Size":[store_size],

            "Customer_Visits":[customer_visits],

            "Product_Price":[product_price],

            "Location_Score":[location_score],

            "Season":[season]

        })

        # ---------------- ENCODING ----------------
        new_data = pd.get_dummies(new_data)

        # ---------------- MATCH TRAINING COLUMNS ----------------
        new_data = new_data.reindex(
            columns=training_columns,
            fill_value=0
        )

        # ---------------- PREDICT ----------------
        prediction = model.predict(new_data)[0]

        # ---------------- COUNTER ANIMATION ----------------
        counter = st.empty()

        step = max(int(prediction / 40), 1)

        for i in range(0, int(prediction), step):

            counter.markdown(
                f"""
                <h1 style='
                text-align:center;
                color:#22c55e;'>
                ₦{i:,.0f}
                </h1>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.02)

        # ---------------- RESULT CARD ----------------
        st.markdown(f"""

        <div style="
        background:rgba(255,255,255,0.10);
        padding:30px;
        border-radius:20px;
        text-align:center;
        animation: fadeIn 1s;
        box-shadow:0 0 20px rgba(0,255,0,0.30);
        margin-top:20px;
        ">

        <h2>📊 Estimated Revenue</h2>

        <h1 style="color:#22c55e;">
        ₦{prediction:,.0f}
        </h1>

        <p>
        AI Powered Revenue Forecast
        </p>

        </div>

        """, unsafe_allow_html=True)

        # ---------------- STATUS ----------------
        if prediction < 5000000:

            st.warning(
                "🟡 Small Business Revenue Level"
            )

        elif prediction < 15000000:

            st.info(
                "🔵 Medium Business Revenue Level"
            )

        else:

            st.success(
                "🟢 Enterprise Revenue Level"
            )

        # ---------------- BAR CHART ----------------
        st.subheader(
            "📈 Revenue Growth Projection"
        )

        levels = [
            "Current",
            "Next Quarter",
            "Next Year"
        ]

        values = [
            prediction,
            prediction * 1.25,
            prediction * 1.60
        ]

        fig, ax = plt.subplots(
            figsize=(5,4)
        )

        ax.bar(levels, values)

        ax.set_title(
            "Business Revenue Growth"
        )

        ax.set_ylabel(
            "Revenue (₦)"
        )

        st.pyplot(fig)

        # ---------------- PIE CHART ----------------
        st.subheader(
            "🥧 Revenue Allocation Insight"
        )

        labels = [
            "Operations",
            "Marketing",
            "Profit"
        ]

        sizes = [45, 30, 25]

        fig2, ax2 = plt.subplots()

        ax2.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        ax2.axis("equal")

        st.pyplot(fig2)

    except Exception as e:

        st.error(
            f"Prediction Error: {e}"
        )

# ---------------- FOOTER ----------------
st.caption(
    "Built with Python • Streamlit • Machine Learning • CEO Dashboard"
)
st.caption("Chart Demostrates how Sales Increases")
st.image('sale.png')
st.caption('Sales Revenue Descriptions')
st.markdown('Sales revenue is the total income a business generates from selling goods or services. Found at the very top of an income statement—earning it the nickname "the top line"—it is calculated by multiplying the number of units sold by their sales price:')
st.image('sales_revenue_product.jpg',width=500)
st.markdown("<center>Project Developed by updateabdullahi</center>", unsafe_allow_html=True)
