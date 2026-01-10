import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Title & Objective
# -------------------------------
st.title("Member C : Visualizations of Sleep, Obstacles and Support Needs")

st.markdown(
    """
    **Objective:**  
    To explore sleep patterns, learning obstacles, and support needs among students 
    in order to understand how lifestyle factors and support systems influence learning effectiveness.
    """
)

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

# -------------------------------
# 1. Bar Chart - Learning Obstacles vs Learning Effectiveness
# -------------------------------
st.subheader("Bar Chart: Learning Obstacles vs Learning Effectiveness")

avg_eff_obstacles = (
    df.groupby("obstacles_index")["learning_effectiveness"]
    .mean()
    .reset_index()
)

fig_bar = px.bar(
    avg_eff_obstacles,
    x="obstacles_index",
    y="learning_effectiveness",
    labels={
        "obstacles_index": "Level of Learning Obstacles",
        "learning_effectiveness": "Average Learning Effectiveness"
    },
    title="Learning Obstacles vs Learning Effectiveness"
    color_discrete_sequence=["#1f77b4"]  # Blue
)

st.plotly_chart(fig_bar, use_container_width=True)

st.markdown(
    """
    **Key Insights:**
    - Lower learning obstacles are linked to higher learning effectiveness.
    - Learning effectiveness declines as obstacles increase.
    - Moderate obstacles already show a negative impact on performance.
    - Reducing learning barriers may improve academic outcomes.
    """
)

# -------------------------------
# 2. Pie Chart - Support Needs Distribution
# -------------------------------
st.subheader("Pie Chart: Distribution of Support Needs")

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

fig_pie = px.pie(
    support_df,
    names="Support Type",
    values="Count",
    title="Distribution of Individual Support Needs Among Students"
)

st.plotly_chart(fig_pie, use_container_width=True)

st.markdown(
    """
    **Key Insights:**
    - Academic and emotional support are the most common needs.
    - A small number of support types dominate student requirements.
    - Support needs vary across students, indicating diverse challenges.
    - Identifying key needs helps prioritize support strategies.
    """
)

# -------------------------------
# 3. Box Plot - Obstacles vs Learning Effectiveness
# -------------------------------
st.subheader("Box Plot: Learning Effectiveness and Obstacles Index")

box_df = df[["learning_effectiveness", "obstacles_index"]].melt(
    var_name="Variable",
    value_name="Value"
)

fig_box = px.box(
    box_df,
    x="Variable",
    y="Value",
    title="Distribution of Learning Effectiveness and Obstacles Index"
)

st.plotly_chart(fig_box, use_container_width=True)

st.markdown(
    """
    **Key Insights:**
    - Learning effectiveness varies widely among students.
    - Some students perform well despite facing obstacles.
    - Obstacles index is more concentrated, showing common challenges.
    - Individual differences influence learning outcomes.
    """
)

# -------------------------------
# 4. Line Chart - Support Index vs Learning Effectiveness
# -------------------------------
st.subheader("Line Chart: Support Index vs Learning Effectiveness")

support_eff = (
    df.groupby("support_index")["learning_effectiveness"]
    .mean()
    .reset_index()
)

fig_line = px.line(
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

st.plotly_chart(fig_line, use_container_width=True)

st.markdown(
    """
    **Key Insights:**
    - Learning effectiveness improves as support increases.
    - Strong support systems are linked to better performance.
    - The trend shows a positive relationship overall.
    - Support plays a crucial role in student success.
    """
)

# -------------------------------
# 5. Scatter Plot - Sleep Quality vs Learning Obstacles
# -------------------------------
st.subheader("Scatter Plot: Sleep Quality vs Learning Obstacles")

fig_scatter = px.scatter(
    df,
    x="sleep_quality",
    y="obstacles_index",
    labels={
        "sleep_quality": "Sleep Quality",
        "obstacles_index": "Obstacles Index"
    },
    title="Sleep Quality vs Learning Obstacles"
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown(
    """
    **Key Insights:**
    - Better sleep quality is associated with fewer obstacles.
    - Poor sleep is linked to higher learning challenges.
    - Sleep is an important lifestyle factor in learning.
    - Improving sleep may help reduce academic difficulties.
    """
)

# -------------------------------
# Conclusion
# -------------------------------
st.subheader("Conclusion")

st.markdown(
    """
    **Conclusion:**  
    The analysis indicates that sleep quality, learning obstacles, and support needs are closely related 
    to students’ learning effectiveness. Better sleep and stronger support systems contribute to improved 
    performance, while increased obstacles negatively affect learning outcomes. Enhancing lifestyle habits 
    and support mechanisms can help improve students’ overall learning effectiveness.
    """
)
