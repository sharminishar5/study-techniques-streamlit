import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Page Title
# -----------------------------
st.title("Page 2 – Stress, Distraction & Motivation")

st.markdown("""
This page analyses how **stress**, **distraction**, and **motivation**
are related to students' learning experiences.
""")

# -----------------------------
# Load Dataset
# -----------------------------
DATA_FILE = "cleaned_student_study_dataset_FINAL.csv"

if not os.path.exists(DATA_FILE):
    st.error("CSV not found! Make sure cleaned_student_study_dataset_FINAL.csv is in the repo root.")
    st.stop()

df = pd.read_csv(DATA_FILE)

# -----------------------------
# Rename Columns (same as Colab)
# -----------------------------
df = df.rename(columns={
    'How often do you experience the following challenges?   [Lack of time]': 'Stress',
    'How often do you experience the following challenges?   [Distractions (phone/social media)]': 'Distraction',
    'How motivated are you to study this semester?': 'Motivation'
})

# -----------------------------
# SECTION 1: Bar Chart
# -----------------------------
st.subheader("1. Average Stress, Distraction & Motivation Levels")

avg_challenges = df[['obs_time', 'obs_distraction', 'obs_motivation']].mean()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(
    ['Stress', 'Distraction', 'Lack of Motivation'],
    avg_challenges.values
)

ax.set_title("Average Stress, Distraction and Motivation Challenges")
ax.set_ylabel("Average Challenge Level")
ax.set_xlabel("Type of Challenge")

st.pyplot(fig)

st.write("""
This bar chart shows the **average level** of stress, distraction,
and lack of motivation experienced by students.
""")

# -----------------------------
# SECTION 2: Heatmap
# -----------------------------
st.subheader("2. Correlation Heatmap")

df_for_heatmap = df[['obs_time', 'obs_distraction', 'Motivation']].copy()
df_for_heatmap = df_for_heatmap.rename(columns={
    'obs_time': 'Stress',
    'obs_distraction': 'Distraction'
})

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    df_for_heatmap.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

ax.set_title("Correlation Between Stress, Distraction and Motivation")
st.pyplot(fig)

st.write("""
The heatmap illustrates the **strength and direction of relationships**
between stress, distraction, and motivation.
""")

# -----------------------------
# SECTION 3: Scatter Plot
# -----------------------------
st.subheader("3. Stress vs Motivation")

fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x='obs_time',
    y='Motivation',
    ax=ax
)

ax.set_xlabel("Stress (Lack of Time)")
ax.set_ylabel("Motivation")
ax.set_title("Relationship Between Stress and Motivation")

st.pyplot(fig)

st.write("""
This scatter plot shows how **motivation changes**
as stress levels increase.
""")

# -----------------------------
# SECTION 4: Box Plot
# -----------------------------
st.subheader("4. Motivation Across Distraction Levels")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(
    data=df,
    x='obs_distraction',
    y='Motivation',
    ax=ax
)

ax.set_xlabel("Distraction Level (Phone / Social Media)")
ax.set_ylabel("Motivation")
ax.set_title("Motivation Across Different Distraction Levels")

st.pyplot(fig)

st.write("""
The box plot compares **motivation levels**
across different levels of distraction.
""")

# -----------------------------
# SECTION 5: Line Chart
# -----------------------------
st.subheader("5. Motivation Trend Across Stress Levels")

stress_motivation = df.groupby('obs_time')['obs_motivation'].mean()

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(
    stress_motivation.index,
    stress_motivation.values,
    marker='o'
)

ax.set_title("Motivation Across Increasing Stress Levels")
ax.set_xlabel("Stress Level")
ax.set_ylabel("Average Lack of Motivation")

st.pyplot(fig)

st.write("""
This line chart highlights how **average motivation**
changes as stress levels increase.
""")
