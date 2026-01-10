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
    "This bar chart shows how often students use different study techniques on average, based on a scale from 1 to 5."
)

st.markdown("""
**Key Insight:**  
* This chart shows the average frequency of study techniques used by students.

* From the chart, we can see that students most frequently use summarising notes, watching videos, doing practice exercises, and reading notes.

* In contrast, techniques such as flashcards and teaching others are used less often.

* This suggests that students prefer familiar and independent study methods rather than more active or collaborative techniques.
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
    "This bar chart shows how effective students believe each study technique is, based on a rating scale from 1 to 5."
)

st.markdown("""
**Key Insight:**  
* This chart shows the perceived effectiveness of different study techniques.

* From the results, practice-based learning has the highest effectiveness score, followed closely by watching educational videos and group study.

* In contrast, flashcards are perceived as less effective compared to other techniques.

* This indicates that students feel they learn better through active engagement, such as practicing and discussing, rather than passive memorisation
""")

st.markdown("---")

# ==================================================
# Visualization 3: Relationship Between Frequency and Effectiveness (Heatmap)
# ==================================================
st.subheader("3️⃣ Relationship Between Frequency and Effectiveness")

corr_cols = [
    "freq_reading","freq_practice","freq_group",
    "eff_reading","eff_practice","eff_group"
]

corr_matrix = df[corr_cols].corr()

fig3 = px.imshow(
    corr_matrix,
    text_auto=True,
    color_continuous_scale="RdBu",
    title="Correlation Between Study Technique Frequency and Effectiveness"
)

st.plotly_chart(fig3, use_container_width=True)

st.caption(
    "This heatmap shows the correlation between how often students use certain study techniques and how effective they perceive those techniques to be."
)

st.markdown("""
**Key Insight:**  
* This heatmap shows the relationship between the frequency of study techniques and their perceived effectiveness.

* Each cell represents the strength of the relationship between two variables, where warmer colors indicate a stronger positive correlation.

* From the heatmap, we can see that practice-based learning and group study show positive correlations between frequency and effectiveness.

* This means that students who use these techniques more often also tend to find them more effective.
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

st.caption(
    "This pie chart shows how students prefer to study."
)

st.markdown("""
**Key Insight:**  
* This pie chart shows students’ preferred study style.

* We can see that almost half of the students prefer switching between studying alone and studying with others, depending on the subject.

* About 38% prefer studying alone, while a smaller group prefers studying mainly with peers.

* This shows that most students do not rely on only one study style and tend to adapt their learning approach based on their needs
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

st.caption(
    "This bar chart shows when students prefer to study, based on their responses in the survey."
)


st.markdown("""
**Key Insight:**  
* This chart shows students’ preferred study time.

* We can see that most students either study late at night or do not have a fixed study time.

* Fewer students prefer studying in the early morning, and only a small number study in the afternoon or evening.

* This suggests that students have different daily routines and often choose study times that fit their personal schedules
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
