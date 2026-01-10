import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dataset Overview")

# Load dataset
df = pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

st.markdown(
    """
    This page provides a general overview of the survey dataset, 
    including respondent demographics and study background.
    """
)

st.markdown("---")

# =======================
# 1. Gender Distribution
# =======================
st.subheader("Gender Distribution")

gender_counts = df["Gender"].value_counts()

fig1, ax1 = plt.subplots()
gender_counts.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Number of Students")
ax1.set_xlabel("Gender")

st.pyplot(fig1)

st.caption("This chart shows the distribution of respondents by gender.")

# =======================
# 2. Level of Study
# =======================
st.subheader("Level of Study")

level_counts = df["Level of Study"].value_counts()

fig2, ax2 = plt.subplots()
level_counts.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Number of Students")
ax2.set_xlabel("Level of Study")

st.pyplot(fig2)

st.caption("This chart presents the distribution of students by level of study.")

# =======================
# 3. Study Hours per Week
# =======================
st.subheader("Study Hours per Week")

fig3, ax3 = plt.subplots()
sns.countplot(
    data=df,
    x="On average, how many hours per week do you study outside of class?",
    ax=ax3
)
ax3.set_xlabel("Study Hours per Week")
ax3.set_ylabel("Number of Students")
plt.xticks(rotation=45)

st.pyplot(fig3)

st.caption("This chart shows how much time students spend studying outside of class.")
