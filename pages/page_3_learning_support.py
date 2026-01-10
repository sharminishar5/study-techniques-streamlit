import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Title & Objective
# -------------------------------
st.title("Visualizations of Sleep, Obstacles and Support Needs")

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
)

st.plotly_chart(fig_bar, use_container_width=True)

st.write(
    "This bar chart illustrates the average learning effectiveness across different levels of learning obstacles. "
    "Students with fewer obstacles tend to achieve higher learning effectiveness. "
    "As learning obstacles increase, learning effectiveness generally declines."
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

st.write(
    "This pie chart shows the distribution of different support needs among students. "
    "Certain types of support are more frequently required, indicating common challenges faced by students. "
    "Less common support needs are grouped under 'Other' for clarity."
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

st.write(
    "The box plot compares the distribution of learning effectiveness and obstacles index. "
    "Learning effectiveness shows greater variability among students. "
    "The obstacles index reflects differences in the level of challenges experienced."
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

st.write(
    "This line chart demonstrates the relationship between support systems and learning effectiveness. "
    "An increasing trend suggests that stronger support systems are associated with better learning outcomes. "
    "This highlights the importance of adequate academic and emotional support."
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

st.write(
    "This scatter plot explores the relationship between sleep quality and learning obstacles. "
    "Students with better sleep quality generally experience fewer learning obstacles. "
    "Poor sleep quality appears to be linked with increased academic challenges."
)
