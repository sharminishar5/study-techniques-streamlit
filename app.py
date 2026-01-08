import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Scientific Visualization Dashboard",
    layout="centered"
)

# Title Section
st.markdown(
    """
    <h1 style='text-align: center;'>JIE42403 SCIENTIFIC VISUALIZATION</h1>
    <h2 style='text-align: center;'>PROJECT</h2>
    <h3 style='text-align: center;'>GROUP 5</h3>
    <br>
    <h2 style='text-align: center;'>STUDENT STUDY TECHNIQUES & LEARNING HABITS SURVEY</h2>
    <br>
    """,
    unsafe_allow_html=True
)

# Members Section
st.markdown(
    """
    <h3>Group Members</h3>
    <ul>
        <li><strong>NURUL AINA BINTI MOHD SAHARANI</strong><br>S22A0039</li>
        <li><strong>NAJWATUL INTAN TASNIM BINTI MOHD ANAFI</strong><br>S22A0085</li>
        <li><strong>SHARMINI A/P SELVAM</strong><br>H22A0060</li>
    </ul>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.info("Please select a page from the sidebar to view each member’s visualization analysis.")
