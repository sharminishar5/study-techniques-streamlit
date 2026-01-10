import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# App Title & Description
# ---------------------------------------------------
st.set_page_config(page_title="Student Learning Effectiveness Analysis", layout="wide")

st.title("📊 Member C Case Study")
st.subheader("Sleep, Learning Obstacles, and Support Needs Analysis")

st.write("""
This dashboard analyzes how **sleep quality**, **learning obstacles**, and **support systems**
influence **students' learning effectiveness**.
""")

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

df = load_data()

st.success("Dataset loaded successfully!")

# ---------------------------------------------------
# Visualization 1: Learning Obstacles vs Learning Effectiveness
# ---------------------------------------------------
st.header("1️⃣ Learning Obstacles vs Learning Effectiveness")

avg_eff_obstacles = df.groupby("obstacles_index")["learning_effectiveness"].mean()

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(avg_eff_obstacles.index.round(2).astype(str), avg_eff_obstacles.values)
ax1.set_xlabel("Level of Learning Obstacles")
ax1.set_ylabel("Average Learning Effectiveness")
ax1.set_title("Learning Obstacles vs Learning Effectiveness")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig1)

st.markdown("""
**Interpretation:**  
Higher obstacle levels tend to be associated with lower learning effectiveness.
""")

# ---------------------------------------------------
# Visualization 2: Distribution of Support Needs (Pie Chart)
# ---------------------------------------------------
st.header("2️⃣ Distribution of Individual Support Needs")

all_support_needs = df["support_needed"].str.split(', ').explode()
individual_support_counts = all_support_needs.value_counts()

N = 7
top_N_supports = individual_support_counts.head(N)
other_supports_count = individual_support_counts.iloc[N:].sum()

if other_supports_count > 0:
    plot_data = pd.concat([top_N_supports, pd.Series({'Other': other_supports_count})])
else:
    plot_data = top_N_supports

fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(
    plot_data.values,
    labels=plot_data.index,
    autopct='%1.1f%%',
    startangle=90
)
ax2.set_title("Distribution of Individual Support Needs")
ax2.axis('equal')

st.pyplot(fig2)

st.markdown("""
**Interpretation:**  
Students most frequently require academic, emotional, and motivational support.
""")

# ---------------------------------------------------
# Visualization 3: Boxplot – Learning Effectiveness vs Obstacles
# ---------------------------------------------------
st.header("3️⃣ Learning Effectiveness vs Learning Obstacles (Boxplot)")

fig3, ax3 = plt.subplots(figsize=(6, 5))
ax3.boxplot(
    [df["learning_effectiveness"], df["obstacles_index"]],
    labels=["Learning Effectiveness", "Obstacles Index"]
)
ax3.set_title("Learning Effectiveness vs Learning Obstacles")

st.pyplot(fig3)

st.markdown("""
**Interpretation:**  
The boxplot highlights variability and potential outliers in learning effectiveness
and obstacle levels among students.
""")

# ---------------------------------------------------
# Visualization 4: Support Systems vs Learning Effectiveness
# ---------------------------------------------------
st.header("4️⃣ Support Systems vs Learning Effectiveness")

support_eff = df.groupby("support_index")["learning_effectiveness"].mean()

fig4, ax4 = plt.subplots(figsize=(8, 5))
ax4.plot(support_eff.index, support_eff.values, marker='o')
ax4.set_xlabel("Support System Index")
ax4.set_ylabel("Learning Effectiveness")
ax4.set_title("Support Systems vs Learning Effectiveness")

st.pyplot(fig4)

st.markdown("""
**Interpretation:**  
Improved support systems are associated with higher learning effectiveness.
""")

# ---------------------------------------------------
# Visualization 5: Sleep Quality vs Learning Obstacles
# ---------------------------------------------------
st.header("5️⃣ Sleep Quality vs Learning Obstacles")

fig5, ax5 = plt.subplots(figsize=(8, 5))
ax5.scatter(df["sleep_quality"], df["obstacles_index"])
ax5.set_xlabel("Sleep Quality")
ax5.set_ylabel("Obstacles Index")
ax5.set_title("Sleep Quality vs Learning Obstacles")

st.pyplot(fig5)

st.markdown("""
**Interpretation:**  
Poor sleep quality is linked to higher learning obstacles, affecting academic performance.
""")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption("Data Analysis Dashboard | Student Learning Effectiveness Study")
