import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Student Learning Effectiveness Analysis",
    layout="wide"
)

sns.set_theme(style="whitegrid")

# ---------------------------------------------------
# Title
# ---------------------------------------------------
st.title("📊 Member C Case Study")
st.subheader("Sleep, Learning Obstacles, and Support Needs")

st.write("""
This dashboard visualizes how **sleep quality**, **learning obstacles**, and **support systems**
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

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=avg_eff_obstacles,
    x="obstacles_index",
    y="learning_effectiveness",
    ax=ax1
)

ax1.set_xlabel("Level of Learning Obstacles")
ax1.set_ylabel("Average Learning Effectiveness")
ax1.set_title("Learning Obstacles vs Learning Effectiveness")

st.pyplot(fig1)

st.markdown("""
**Interpretation:**  
An increase in learning obstacles is generally associated with a decrease in
students’ learning effectiveness.
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

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=support_df,
    x="Count",
    y="Support Type",
    ax=ax2
)

ax2.set_title("Distribution of Individual Support Needs")
ax2.set_xlabel("Number of Students")
ax2.set_ylabel("Support Type")

st.pyplot(fig2)

st.markdown("""
**Interpretation:**  
Academic, emotional, and motivational supports are the most commonly required
among students.
""")

# ---------------------------------------------------
# 3. Boxplot: Learning Effectiveness vs Obstacles
# ---------------------------------------------------
st.header("3️⃣ Learning Effectiveness vs Learning Obstacles")

boxplot_df = df[["learning_effectiveness", "obstacles_index"]].melt(
    var_name="Variable",
    value_name="Score"
)

fig3, ax3 = plt.subplots(figsize=(7, 5))
sns.boxplot(
    data=boxplot_df,
    x="Variable",
    y="Score",
    ax=ax3
)

ax3.set_title("Learning Effectiveness vs Learning Obstacles")

st.pyplot(fig3)

st.markdown("""
**Interpretation:**  
The boxplot shows variation and outliers, indicating differences in obstacle levels
and learning effectiveness among students.
""")

# ---------------------------------------------------
# 4. Support Systems vs Learning Effectiveness
# ---------------------------------------------------
st.header("4️⃣ Support Systems vs Learning Effectiveness")

support_eff = (
    df.groupby("support_index", as_index=False)["learning_effectiveness"]
    .mean()
)

fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.lineplot(
    data=support_eff,
    x="support_index",
    y="learning_effectiveness",
    marker="o",
    ax=ax4
)

ax4.set_xlabel("Support System Index")
ax4.set_ylabel("Learning Effectiveness")
ax4.set_title("Support Systems vs Learning Effectiveness")

st.pyplot(fig4)

st.markdown("""
**Interpretation:**  
Higher support system levels are associated with better learning effectiveness.
""")

# ---------------------------------------------------
# 5. Sleep Quality vs Learning Obstacles
# ---------------------------------------------------
st.header("5️⃣ Sleep Quality vs Learning Obstacles")

fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="sleep_quality",
    y="obstacles_index",
    ax=ax5
)

ax5.set_xlabel("Sleep Quality")
ax5.set_ylabel("Obstacles Index")
ax5.set_title("Sleep Quality vs Learning Obstacles")

st.pyplot(fig5)

st.markdown("""
**Interpretation:**  
Poor sleep quality tends to be associated with higher learning obstacles.
""")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption("Student Learning Effectiveness Dashboard | Member C Case Study")
