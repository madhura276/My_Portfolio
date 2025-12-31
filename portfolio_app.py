import streamlit as st
from PIL import Image

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Madhura's Portfolio",
    page_icon="💻",
    layout="wide"
)

# ---------------- Sidebar Navigation ----------------
st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🛠 Skills", "📂 Projects", "📬 Contact"])

# ---------------- HOME ----------------
if page == "🏠 Home":
    st.title("👋 Hi, I'm Madhura Gundluru")
    st.subheader("Aspiring Data Scientist | Machine Learning | AI Enthusiast")

    st.write("""
    Welcome to my portfolio!  
    I’m passionate about **Data Science, Machine Learning, and AI**.  
    I love anime (Naruto 🌀), dance 💃, and exploring new technologies.  
    """)

    image = Image.open("Madhura.jpg")
    st.image(image, width=200, caption="Madhura Gundluru")

    with open("Madhura_new.pdf", "rb") as file:
        st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Madhura_Resume.pdf",
            mime="application/pdf"
        )

# ---------------- SKILLS ----------------
elif page == "🛠 Skills":
    st.header("🛠 Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Programming")
        st.markdown("""
        - Python  
        - JavaScript  
        - HTML, CSS
        """)

        st.subheader("Data Science & ML / AI")
        st.markdown("""
        - Data Analysis: Pandas, NumPy  
        - Machine Learning: Scikit-learn  
        - Deep Learning (Basics): TensorFlow  
        - NLP & Text Similarity  
        """)

    with col2:
        st.subheader("Web Development & Frameworks")
        st.markdown("""
        - Frontend: React  
        - Backend: Django, Node.js  
        - Database: MongoDB  
        """)

        st.subheader("Tools & Platforms")
        st.markdown("""
        - Streamlit  
        - Power BI, Excel  
        - Git & GitHub  
        """)

        st.subheader("Behavioural Skills")
        st.markdown("""
        - Time Management  
        - Adaptability  
        """)

# ---------------- PROJECTS ----------------
elif page == "📂 Projects":
    st.header("📂 Projects Showcase")

    project_list = [
        {
            "title": "Smart Career Recommendation System (AI-Based)",
            "skills": [
                "Python", "Data Science", "Machine Learning",
                "TF-IDF", "Cosine Similarity", "Explainable AI",
                "React", "Node.js", "MongoDB", "Tailwind CSS"
            ],
            "desc": [
                "Built an AI-based career recommendation system using Data Science and Machine Learning.",
                "Applied TF-IDF vectorization and cosine similarity for semantic skill matching.",
                "Implemented a hybrid scoring approach combining skill overlap and ML similarity.",
                "Designed Explainable AI insights to justify recommendations clearly.",
                "Identified skill gaps and suggested improvements for upskilling.",
                "Developed an end-to-end system using Python, Node.js, MongoDB, React, and Tailwind CSS."
            ],
            "link": "https://github.com/madhura276/smart-career-recommendation-system"
        },
        {
            "title": "📈 Data Analysis with Pandas & NumPy",
            "skills": ["Python", "Pandas", "NumPy", "EDA"],
            "desc": [
                "Performed data cleaning and preprocessing.",
                "Conducted exploratory data analysis.",
                "Extracted insights using Pandas and NumPy."
            ],
            "link": "https://github.com/madhura276/Netflix_Data_Analysis"
        },
        {
            "title": "📊 SMS Spam Detection",
            "skills": ["Python", "Machine Learning", "NLP"],
            "desc": [
                "Built an NLP-based ML classifier.",
                "Classified messages as Spam or Not Spam."
            ],
            "link": "https://github.com/madhura276/SMS-Spam-Detection"
        }
    ]

    for project in project_list:
        st.subheader(project["title"])

        st.markdown("**Skills:** " + ", ".join(project["skills"]))

        for point in project["desc"]:
            st.markdown(f"- {point}")

        st.markdown(f"[🔗 View Project]({project['link']})")
        st.markdown("---")

# ---------------- CONTACT ----------------
elif page == "📬 Contact":
    st.header("📬 Get in Touch")

    st.markdown("""
    - 📧 Email: g.madhura.tech@gmail.com  
    - 💼 LinkedIn: [Madhura Gundluru](https://www.linkedin.com/in/madhura-gundluru/)  
    - 🐙 GitHub: [madhura276](https://github.com/madhura276)  
    """)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send Message 🚀")
