import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Member A – Study Techniques & Effectiveness",
    layout="wide"
)

# --------------------------------------------------
# Title & Objective
# --------------------------------------------------
st.title("Member A: Study Techniques & Learning Effectiveness")

st.markdown("""
### Objective
To analyze the **frequency** and **perceived effectiveness** of different study techniques used by students,
based on survey responses.
""")

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_student_study_dataset_FINAL.csv")

df = load_data()

st.markdown("---")

# ==================================================
# Visualization 1: Frequency of Study Techniques
# ==================================================
st.subheader("1️⃣ Average Frequency of Study Techniques Used")

freq_cols = [
    "freq_reading","freq_videos","freq_practice","freq_group",
    "freq_summary","freq_flashcards","freq_teaching"
]

freq_means = (
    df[freq_cols]
    .mean()
    .reset_index()
    .rename(columns={"index": "Study Technique", 0: "Average Frequency"})
)

fig1 = px.bar(
    freq_means,
    x="Study Technique",
    y="Average Frequency",
    text_auto=True,
    title="Average Frequency of Study Techniques Used by Students"
)

fig1.update_layout(
    yaxis_title="Average Frequency Score (1–5)",
    xaxis_title=""
)

st.plotly_chart(fig1, use_container_width=True)

st.caption(
    "This chart shows how often students use different study techniques on average."
)

st.markdown("""
**Key Insight:**  
Students tend to rely more on familiar techniques such as reading notes, watching videos,
and doing practice exercises, while techniques like teaching others and flashcards are used less frequently.
""")

st.markdown("---")

# ==================================================
# Visualization 2: Perceived Effectiveness
# ==================================================
st.subheader("2️⃣ Perceived Effectiveness of Study Techniques")

eff_cols = [
    "eff_reading","eff_practice","eff_group",
    "eff_flashcards","eff_videos"
]

eff_means = (
    df[eff_cols]
    .mean()
    .reset_index()
    .rename(columns={"index": "Study Technique", 0: "Effectiveness Score"})
)

fig2 = px.bar(
    eff_means,
    x="Study Technique",
    y="Effectiveness Score",
    text_auto=True,
    color="Effectiveness Score",
    color_continuous_scale="Blues",
    title="Perceived Effectiveness of Study Techniques"
)

fig2.update_layout(
    yaxis_title="Effectiveness Score (1–5)",
    xaxis_title=""
)

st.plotly_chart(fig2, use_container_width=True)

st.caption(
    "This visualization highlights which study techniques students perceive as most effective."
)

st.markdown("""
**Key Insight:**  
Practice-based techniques and group study receive higher effectiveness ratings,
suggesting that active learning strategies are more beneficial than passive ones.
""")

st.markdown("---")

# ==================================================
# Visualization 3: Frequency vs Effectiveness
# ==================================================
st.subheader("3️⃣ Relationship Between Frequency and Effectiveness")

comparison = freq_means.merge(eff_means, on="Study Technique")

fig3 = px.scatter(
    comparison,
    x="Average Frequency",
    y="Effectiveness Score",
    size="Effectiveness Score",
    color="Effectiveness Score",
    text="Study Technique",
    title="Frequency vs Perceived Effectiveness of Study Techniques"
)

fig3.update_traces(textposition="top center")

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
**Key Insight:**  
Some techniques are frequently used but not perceived as highly effective,
indicating a gap between students’ study habits and optimal learning strategies.
""")

st.markdown("---")

# ==================================================
# Visualization 4: Study Preference
# ==================================================
st.subheader("4️⃣ Study Preference: Alone vs With Others")

pref_counts = df["study_preference"].value_counts().reset_index()
pref_counts.columns = ["Study Preference", "Number of Students"]

fig4 = px.pie(
    pref_counts,
    names="Study Preference",
    values="Number of Students",
    title="Study Preference Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
**Key Insight:**  
While many students prefer studying alone, a significant proportion still value group study,
highlighting the importance of both independent and collaborative learning environments.
""")

st.markdown("---")

# ==================================================
# Visualization 5: Preferred Study Time
# ==================================================
st.subheader("5️⃣ Preferred Study Time")

time_counts = df["study_time"].value_counts().reset_index()
time_counts.columns = ["Study Time", "Number of Students"]

fig5 = px.bar(
    time_counts,
    x="Study Time",
    y="Number of Students",
    text_auto=True,
    title="Preferred Study Time Among Students"
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
**Key Insight:**  
Students exhibit varied study time preferences, suggesting that flexible learning schedules
may better support different study habits.
""")

st.markdown("---")

# ==================================================
# Conclusion
# ==================================================
st.subheader("Conclusion (Member A)")

st.markdown("""
The analysis reveals that students use a variety of study techniques,
but frequently used methods are not always perceived as the most effective.
Active learning strategies such as practice exercises and group discussions
tend to provide greater perceived learning benefits.

These findings emphasize the need to guide students toward more effective
study strategies rather than relying solely on habitual methods.
""")
