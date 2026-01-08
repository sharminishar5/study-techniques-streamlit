import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Page Title
# -----------------------------
st.title("Stress, Distraction & Motivation by Sharmini")

st.markdown("""
This section presents visualizations related to stress, distraction, and motivation factors among students. The visualizations aim to explore how these factors influence student’s learning experiences and academic engagement. By applying appropriate scientific visualization techniques, patterns, trends, and variations in stress levels, sources of distraction, and motivation can be clearly identified and interpreted to support data driven insights.
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
st.subheader("1. Bar Chart of Average Stress, Distraction and Motivation Challenges")

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

st.markdown("""
<p style="text-align: justify;">
The bar chart titled <b>Average Stress, Distraction and Motivation Challenges</b> shows the average level of three main academic problems faced by students, which are stress, distraction, and lack of motivation. Each bar represents the average level of challenge as reported by the students. According to the chart, distraction has the highest average value of about more than 3.5, thus the greatest challenge that students have to go through. It implies that constant phone call distractions and social networks, noise in the environment, and multitasking among other factors have a massive influence on the ability of students to study effectively and concentrate. The second most challenging issue is the lack of motivation with an average score of approximately 3.5, which implies that a significant portion of the population of students has to encounter the problem of inability to remain consistently engaged and enthusiastic about their studies. Stress also has the lowest average as it is between 3.0 and 3.5, meaning that despite the academic pressure and lack of time, it is not seen as a major problem compared to distraction and motivational problems. Generally, the bar chart serves to point out that distraction is the most prevalent academic issue, which is succeeded by a lack of motivation and stress, successfully showing the comparative difference of the influences of the factors on the academic experience of students.
</p>
""", unsafe_allow_html=True)

# -----------------------------
# SECTION 2: Heatmap
# -----------------------------
st.subheader("2. Heatmap of Correlation Between Stress, Distraction and Motivation")

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

st.markdown("""
<p style="text-align: justify;">
The heatmap shows the correlation between stress, distraction, and motivation. It shows that stress and distraction are moderately to strongly positively related (r = 0.64); students who report a higher level of stress are also more likely to be distracted, which implies that stress and lack of focus are tightly connected. However, stress and motivation share a very weak positive correlation (r = 0.12), indicating that stress has little meaningful relationship with how motivated students feel. Some students may become slightly more driven under stress while others may feel discouraged, so the overall trend is low. Lastly, there is practically no correlation between distraction and motivation (r = -0.019); students can be motivated and distracted by phones or the environment, or unmotivated without feeling distracted. Generally, the key conclusion is that the stress factor is strongly correlated with distraction, whereas motivation does not seem to be very dependent on stress and distraction in this study.
</p>
""", unsafe_allow_html=True)

# -----------------------------
# SECTION 3: Motivation Level Frequency
# -----------------------------
st.subheader("3. Bar Chart of Motivation Level Frequency")

# Count frequency of motivation levels
motivation_counts = df["Motivation"].value_counts().sort_index()

# Create the bar chart (default color)
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(motivation_counts.index, motivation_counts.values)  # default blue
ax.set_xlabel("Motivation Level")
ax.set_ylabel("Number of Students")
ax.set_title("Motivation Level Frequency")
plt.xticks(rotation=0, ha='center')

# Display bar chart in Streamlit
st.pyplot(fig)

st.markdown("""
<p style="text-align: justify;">
The bar chart shows <b>Motivation Level Frequency</b> of students. The frequency of students in 5 levels of self-reported motivation, where level 1 indicates not motivated and level 5 indicates highly motivated. There is a high positive skew with more students indicating high levels of motivation, with the highest number of students (about 30-35) at level 5. This shows that a good percentage of the student body is quite determined to study, meaning they are well engaged and motivated. Following that, the frequency decreases distinctly with lower motivation levels. Approximately 15-20 students report level 4, which is still quite high. Levels 3 and 2 show decreasing numbers of students, indicating that a smaller percentage is moderately or slightly motivated. The lowest bar, representing level 1, shows that very few students are entirely unmotivated. Overall, the chart is a promising sign of student motivation as most students are concentrated at the upper part of the scale. However, the presence of students at lower motivational levels (1-3) shows the need for targeted interventions to help them engage, focus, and stay motivated. The distribution indicates that although a majority are self-motivated, academic programs might maximize outcomes by adopting motivational supports such as mentoring, goal-setting workshops, or interactive learning strategies to assist less motivated students.
</p>
""", unsafe_allow_html=True)

# -----------------------------
# SECTION 4: Box Plot
# -----------------------------
st.subheader("4. Box plot of Motivation Across Different Distraction Levels")

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

st.markdown("""
<p style="text-align: justify;">
This box plot represents the relationship between student motivation and the levels of distraction reported from phone and social media usage. The visualization shows an obvious negative tendency of motivation as distraction levels rise. Students with low levels of distraction (to the left of the x-axis) have higher median motivation scores, often concentrated around 4 or 5. This implies that students who can reduce digital distractions are more likely to feel engaged, focused, and motivated in their learning. Conversely, median motivation significantly decreases as distraction levels increase. At moderate and high distraction levels, median motivation scores drop to approximately 3 or less, and the distribution becomes wider, indicating higher variability in student motivation. This means that some students may remain comparatively motivated despite distractions, while others experience a major decline in motivation and interest. The occurrence of outliers at different distraction levels, particularly at higher motivation levels even with moderate distraction, indicates that some students might have effective strategies or strong intrinsic motivation that helps them maintain focus. Overall, the visualization strongly suggests that phone and social media distractions negatively influence academic motivation.
</p>
""", unsafe_allow_html=True)

# -----------------------------
# SECTION 5: Line Chart
# -----------------------------
st.subheader("5. Line Chart of Stress Level Across Different Distraction Levels")

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

st.markdown("""
<p style="text-align: justify;">
This line chart shows the stress level across different distraction levels, which scale between 1 and 5 (1 being low distraction and 5 being high distraction). Stress levels are mapped as follows: 1 = never, 2 = rarely, 3 = sometimes, 4 = often, and 5 = very often. The graph demonstrates a positive relationship between distraction and stress. Average stress levels increase steadily as distraction rises from 1 to 5. Students with low distraction levels (approximately 1-2) are the least stressed, indicating their stress is manageable when they can concentrate and avoid distractions. At moderate distraction levels (~3), stress levels begin to rise. At higher distraction levels (4-5), stress peaks, implying that frequent disruptions—especially from phones, social media, or environmental noise—contribute significantly to student stress. The more a person is distracted, the more stress they report, forming a cyclic pattern where distractions reduce focus, increase study time, and cause anxiety about performance. This visualization emphasizes the importance of controlling distractions to reduce student stress. Programs encouraging digital discipline, focused study areas, and mindful device use may be effective in mitigating stress.
</p>
""", unsafe_allow_html=True)

