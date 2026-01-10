import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dataset Overview",
    layout="wide"
)

st.title("Dataset Overview")

st.markdown("""
This page provides an **interactive overview** of the survey dataset,
including respondent demographics and study background.
""")

st.markdown("---")

# --------------------------------------------------
# Load dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

df = load_data()

# --------------------------------------------------
# Dataset preview (interactive table)
# --------------------------------------------------
st.subheader("📄 Survey Dataset Preview")

st.markdown(
    "You can scroll, sort, and explore the cleaned survey dataset below."
)

st.dataframe(df, use_container_width=True)

st.markdown("---")

# --------------------------------------------------
# Filters (Optional but VERY GOOD)
# --------------------------------------------------
st.subheader("🔎 Filter Responses")

col1, col2 = st.columns(2)

with col1:
    selected_gender = st.multiselect(
        "Select Gender:",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
    )

with col2:
    selected_level = st.multiselect(
        "Select Level of Study:",
        options=df["Level of Study"].unique(),
        default=df["Level of Study"].unique()
    )

filtered_df = df[
    (df["Gender"].isin(selected_gender)) &
    (df["Level of Study"].isin(selected_level))
]

st.caption(f"Filtered dataset size: **{len(filtered_df)} respondents**")

st.markdown("---")

# ==================================================
# 1. Gender Distribution
# ==================================================
st.subheader("1️⃣ Gender Distribution")

gender_counts = filtered_df["Gender"].value_counts().reset_index()
gender_counts.columns = ["Gender", "Number of Students"]

fig1 = px.bar(
    gender_counts,
    x="Gender",
    y="Number of Students",
    text_auto=True,
    title="Gender Distribution of Respondents"
)

st.plotly_chart(fig1, use_container_width=True)

st.caption(
    "This chart shows the distribution of respondents by gender."
)

st.markdown("---")

# ==================================================
# 2. Level of Study
# ==================================================
st.subheader("2️⃣ Level of Study")

level_counts = filtered_df["Level of Study"].value_counts().reset_index()
level_counts.columns = ["Level of Study", "Number of Students"]

fig2 = px.bar(
    level_counts,
    x="Level of Study",
    y="Number of Students",
    text_auto=True,
    title="Distribution of Students by Level of Study"
)

st.plotly_chart(fig2, use_container_width=True)

st.caption(
    "This chart presents the distribution of students by their level of study."
)

st.markdown("---")

# ==================================================
# 3. Study Hours per Week
# ==================================================
st.subheader("3️⃣ Study Hours per Week (Outside Class)")

study_hours_counts = (
    filtered_df["On average, how many hours per week do you study outside of class?"]
    .value_counts()
    .reset_index()
)

study_hours_counts.columns = ["Study Hours", "Number of Students"]

fig3 = px.bar(
    study_hours_counts,
    x="Study Hours",
    y="Number of Students",
    text_auto=True,
    title="Weekly Study Hours Outside of Class"
)

fig3.update_layout(
    xaxis_title="Study Hours Category",
    yaxis_title="Number of Students"
)

st.plotly_chart(fig3, use_container_width=True)

st.caption(
    "This chart illustrates how much time students spend studying outside of class."
)

st.markdown("---")

# --------------------------------------------------
# Summary
# --------------------------------------------------
st.subheader("Summary")

st.markdown("""
- The dataset consists of responses from students with diverse backgrounds and study levels.
- Interactive filters allow deeper exploration of demographic trends.
- Understanding the respondent profile provides important context for interpreting
  the subsequent analysis conducted by each group member.
""")
