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
Academic, emotional, and motivational supports are the most frequently reported needs.  
This highlights the importance of holistic support systems in improving students’ learning experiences.
""")

# ---------------------------------------------------
# 3. Learning Effectiveness vs Learning Obstacles (Boxplot)
# ---------------------------------------------------
st.header("3️⃣ Learning Effectiveness vs Learning Obstacles")

boxplot_df = df[["learning_effectiveness", "obstacles_index"]].melt(
    var_name="Variable",
    value_name="Score"
)

fig3 = px.box(
    boxplot_df,
    x="Variable",
    y="Score",
    title="Learning Effectiveness vs Learning Obstacles"
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Interpretation:**  
The boxplot compares the distribution and variability of learning effectiveness and learning obstacles.  
Noticeable differences in spread and outliers suggest unequal learning conditions among students.  
Students facing higher obstacles may experience reduced learning effectiveness.
""")

# ---------------------------------------------------
# 4. Support Systems vs Learning Effectiveness
# ---------------------------------------------------
st.header("4️⃣ Support Systems vs Learning Effectiveness")

support_eff = (
    df.groupby("support_index", as_index=False)["learning_effectiveness"]
    .mean()
)

fig4 = px.line(
    support_eff,
    x="support_index",
    y="learning_effectiveness",
    markers=True,
    labels={
        "support_index": "Support System Index",
        "learning_effectiveness": "Learning Effectiveness"
    },
    title="Support Systems vs Learning Effectiveness"
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
**Interpretation:**  
The line chart demonstrates a positive relationship between support systems and learning effectiveness.  
Learning effectiveness increases as the level of support systems improves.  
This emphasizes the critical role of institutional and social support in student success.
""")

# ---------------------------------------------------
# 5. Sleep Quality vs Learning Obstacles
# ---------------------------------------------------
st.header("5️⃣ Sleep Quality vs Learning Obstacles")

fig5 = px.scatter(
    df,
    x="sleep_quality",
    y="obstacles_index",
    labels={
        "sleep_quality": "Sleep Quality",
        "obstacles_index": "Obstacles Index"
    },
    title="Sleep Quality vs Learning Obstacles"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
**Interpretation:**  
The scatter plot illustrates the relationship between sleep quality and learning obstacles.  
Students with poorer sleep quality tend to experience higher levels of learning obstacles.  
This suggests that inadequate sleep may contribute to increased academic challenges.
""")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("---")
st.caption("Student Learning Effectiveness Dashboard | Member C Case Study")
