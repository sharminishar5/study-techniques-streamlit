import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Student Learning Effectiveness Analysis",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("📊 Member C Case Study")
st.subheader("Sleep, Learning Obstacles, and Support Needs")

st.write("""
This dashboard examines how **sleep quality**, **learning obstacles**, and **support systems**
influence **students’ learning effectiveness**.
""")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

df = load_data()
st.success("Dataset loaded successfully")

# ---------------------------------------------------
# 1. Learning Obstacles vs Learning Effectiveness
# ---------------------------------------------------
st.header("1️⃣ Learning Obstacles vs Learning Effectiveness")

avg_eff_obstacles = (
    df.groupby("obstacles_index", as_index=False)["learning_effectiveness"]
    .mean()
)

fig1 = px.bar(
    avg_eff_obstacles,
    x="obstacles_index",
    y="learning_effectiveness",
    labels={
        "obstacles_index": "Level of Learning Obstacles",
        "learning_effectiveness": "Average Learning Effectiveness"
    },
    title="Learning Obstacles vs Learning Effectiveness"
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
**Interpretation:**  
The bar chart illustrates the relationship between learning obstacles and students’ learning effectiveness.  
As the level of learning obstacles increases, the average learning effectiveness generally decreases.  
This indicates that higher academic or personal barriers negatively impact students’ learning outcomes.
""")

# ---------------------------------------------------
# 2. Distribution of Individual Support Needs
# ---------------------------------------------------
st.header("2️⃣ Distribution of Individual Support Needs")

all_support_needs = df["support_needed"].str.split(", ").explode()
support_counts = all_support_needs.value_counts()

N = 7
top_supports = support_counts.head(N)
other_count = support_counts.iloc[N:].sum()

if other_count > 0:
    plot_data = pd.concat([top_supports, pd.Series({"Other": other_count})])
else:
    plot_data = top_supports

support_df = plot_data.reset_index()
support_df.columns = ["Support Type", "Count"]

fig2 = px.bar(
    support_df,
    x="Count",
    y="Support Type",
    orientation="h",
    title="Distribution of Individual Support Needs",
    labels={"Count": "Number of Students"}
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**Interpretation:**  
The chart shows the most common types of support required by students.  
Academic, emotional, and motivational supports are the most freq
