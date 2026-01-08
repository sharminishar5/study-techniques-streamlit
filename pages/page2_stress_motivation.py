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

st.write("""
The bar chart titled Average Stress, Distraction and Motivation Challenges shows the average level of three main academic problems faced by students which is stress, distraction, and lack of motivation. Each bar represents the average level of challenge as reported by the students. According to the chart, distraction has the highest average value of about more than 3.5 thus the greatest challenge that students have to go through. It implies that constant phone call distractions and social networks, noise in the environment, and multitasking among other factors have a massive influence on the ability of students to study effectively and concentrate. The second most challenging issue is the lack of motivation with an average score of approximately 3.5, which implies that a significant portion of the population of students has to encounter the problem of inability to remain consistently engaged and enthusiastic about their studies. Stress also has the lowest average as it is at between 3.0 and 3.5 meaning that despite the academic pressure and lack of time, it is not seen as a major problem as distraction and motivational problems. Generally, the bar chart serves to point out that distraction is the most prevalent academic issue, which is succeeded by a lack of motivation and stress, which successfully makes the comparative difference of the influences of the factors on the academic experience of students.
""")

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

st.write("""
The heatmap shows correlation between stress, distraction and motivation. It shows that the stress and distraction are moderate to strongly positively related (r = 0.64), students who report a higher level of stress are also more likely to be distracted, which implies that stress and lack of focus are tightly connected. However, stress and motivation share a very weak positive correlation (r = 0.12), which indicates that stress has little meaningful relationship with how motivated students feel. Some students may become slightly more driven under stress while others may feel discouraged, so the overall trend is low. Lastly, there is practically no correlation between distraction and motivation (r = -0.019), students can be motivated and distracted  by phones or the environment, or unmotivated without feeling distracted. Generally, the key conclusion is that the stress factor is strongly correlated with distraction, whereas motivation does not seem to be very dependent on stress and distraction in this study.
""")

# -----------------------------
# SECTION 3: Motivation Level Frequency
# -----------------------------
st.subheader("3. Bar Chart of Motivation Level Frequency")

# Count frequency of motivation levels
motivation_counts = df["Motivation"].value_counts().sort_index()

# Create the bar chart
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(motivation_counts.index, motivation_counts.values, color='skyblue')
ax.set_xlabel("Motivation Level")
ax.set_ylabel("Number of Students")
ax.set_title("Motivation Level Frequency")
plt.xticks(rotation=0, ha='center')

# Display bar chart in Streamlit
st.pyplot(fig)

# Add explanation
st.write("""
The bar chart shows Motivation Level Frequency of students. The frequency of students in 5 levels of self reported motivation, the 1 level is indicating not motivated and the level 5 is highly motivated. There is a high positive skew with more motivation level indicating high levels of motivation with the highest number of students of about 30-35 indicating a level of motivation as 5. It shows that a good percentage of the student body is quite determined to study which means that they are well engaged and motivated to study. After that, the frequency of occurrence decreases distinctly with the drop in motivation levels. The other students on approximately 15-20 of them report level 4 for motivation, which is still quite a high level of motivation. The level 3 and 2 of motivation have decreasing numbers of students, indicating that the smaller percent is moderately or slightly motivated. The lowest bar, which represents the level of motivation 1, shows that a very few students do not identify with being entirely not motivated. Overall, the chart is a promising sign of student motivation as most students are concentrated at the upper part of the motivation scale. However, the fact that students are at lower motivational rates particularly, levels 1-3 shows the possibility of specific intervention that will help the struggling students to cope with their inability to engage, be focused, or be motivated. The distribution indicates that although a majority of students are self-motivated, the academic programs might be able to maximize the results by adopting motivational supports, including mentoring, goal setting workshops, or interactive learning strategies, to suit those students who are less motivated.
""")


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

st.write("""
This box plot represents the relationship between student motivation and the levels of distraction reported to occur with phone and social media usage. The visualization shows the obvious negative tendency of motivation in regard to the rise of the levels of distraction. The students with low levels of distraction which are to the left of the x-axis have higher median scores of motivation which is often concentrated towards 4 or 5. This implies that students that can reduce digital distractions are more likely to feel involved, concentrated and motivated in their learning. On the other side, the median motivation is significantly reduced as the distraction levels increase. The median scores of motivation at moderate and high levels of distraction goes down to approximately 3 or less, and the distribution of scores becomes wider, which means the higher variability in motivation levels of students. This is to say that some students may still be comparatively motivated despite their distractors, but some suffer a major loss in their motivation and interest. The occurrence of outliers at the different levels of distraction and more so at higher levels of motivation even when moderate distraction is involved, is an indication that some students might have effective strategies or that they might have strong motivation which aids them to maintain their focus despite distraction. The visualization gives a strong argument to the fact that phone and social media distractions have a negative influence on academic motivation. 
""")

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

st.write("""
This line chart shows the stress level across different distraction levels which scale between 1 and 5 with 1 being low distraction and 5 being high distraction. Stress level mapping used 1 for never, 2 for rarely, 3 represents sometimes, 4 represents often and 5 is for very often. The graph demonstrates that there is a positive relationship between distraction and stress. The average levels of stress increase steadily with a rise in the level of distraction between 1-5. Students with low distraction levels approximately 1-2 at the scale are the least stressed and it means that their stress is quite manageable when they are able to concentrate and not to be distracted. However, at the moderate levels of distraction about 3, the levels of stress start to gain. When the distraction is higher between 4-5, stress peaks, which implies that a frequent disruption, especially through phones, social media or even the noise of the environment, is a serious contributor to a high level of stress among students. The more a person is distracted, the more they report stress, and so it forms a cyclic pattern where distractions cause loss of focus, spend more time on studying, and experience anxiety over performance. The visualization emphasizes that it is very important to control distractions in order to calm the pressure of students. Digital discipline programs, encouraging concentration in the study area and developing mind centered device use might be effective in reducing stress. 
""")
