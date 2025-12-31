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

    # Profile Image (centered)
    image = Image.open("Madhura.jpg")  # Make sure file is in same folder
    st.image(image, width=200, caption="Madhura Gundluru", use_container_width=False)

    # Resume download
    with open("Madhura_new.pdf", "rb") as file:  # Make sure file is in same folder
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
        st.write("""
        - Python  
        - JavaScript  
        - HTML, CSS
        """)
    
        st.subheader("Data Science & ML / AI")
        st.write("""
        - Data Analysis: Pandas, NumPy  
        - Machine Learning: Scikit-learn  
        - Deep Learning (Basics): TensorFlow  
        - NLP & Text Similarity  
        """)

    with col2:
        st.subheader("Web Development & Frameworks")
        st.write("""
        - Frontend: React  
        - Backend: Django, Node.js  
        - Database: MongoDB  
        """)
    
        st.subheader("Tools & Platforms")
        st.write("""
        - Streamlit  
        - Power BI, Excel  
        - Git & GitHub  
        """)

        st.subheader("Behavioural Skills")
        st.write("""
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
        "skills": ["Python", "Pandas", "NumPy", "EDA", "Data Cleaning"],
        "desc": [
            "Performed data cleaning and preprocessing on real-world datasets.",
            "Conducted exploratory data analysis to extract insights.",
            "Used Pandas and NumPy for efficient data manipulation."
        ],
        "link": "https://github.com/madhura276/Netflix_Data_Analysis"
    },

    {
        "title": "📊 SMS Spam Detection",
        "skills": ["Python", "Machine Learning", "NLP", "Scikit-learn"],
        "desc": [
            "Built a Machine Learning model using NLP techniques.",
            "Classified messages as Spam or Not Spam.",
            "Applied text preprocessing and feature extraction methods."
        ],
        "link": "https://github.com/madhura276/SMS-Spam-Detection"
    },

    {
        "title": "Exploratory Data Analysis (EDA) on Iris Dataset 🌸",
        "skills": ["Python", "Pandas", "Matplotlib", "Seaborn", "EDA"],
        "desc": [
            "Performed detailed exploratory data analysis on the Iris dataset.",
            "Analyzed feature distributions and relationships across species.",
            "Created visualizations using Matplotlib and Seaborn."
        ],
        "link": "https://github.com/madhura276/Iris_Data_Analysis"
    },

    {
        "title": "🛒 Online Shopping Cart",
        "skills": ["Python", "Application Logic", "OOP"],
        "desc": [
            "Developed a shopping cart system with product listing functionality.",
            "Implemented cart updates and checkout simulation.",
            "Focused on core application logic and user flow."
        ],
        "link": "https://github.com/madhura276/Online-Shopping-Cart"
    },

    {
        "title": "🎓 Student Score Manager",
        "skills": ["Python", "File Handling", "Data Analysis"],
        "desc": [
            "Built a Python-based file handling project.",
            "Managed and analyzed student scores.",
            "Implemented data storage and retrieval using files."
        ],
        "link": "https://github.com/madhura276/student-management-system"
    },

    {
        "title": "Student CRUD Application with Python & MySQL",
        "skills": ["Python", "MySQL", "CRUD Operations", "Database"],
        "desc": [
            "Developed a menu-driven Python application.",
            "Implemented full CRUD operations for student records.",
            "Integrated MySQL database for persistent data storage."
        ],
        "link": "https://github.com/madhura276/Student-CRUD-Python-"
    },

    {
        "title": "React Profile App",
        "skills": ["React", "JavaScript", "React Router", "CSS"],
        "desc": [
            "Built a profile management web application using React.",
            "Implemented routing with React Router.",
            "Used state management and clean CSS styling."
        ],
        "link": "https://github.com/madhura276/React-Profile-App"
    },

    {
        "title": "🩺 Cervical Cancer Detection",
        "skills": ["Machine Learning", "Python", "Healthcare AI", "Research"],
        "desc": [
            "AI-driven academic project based on IEEE research papers.",
            "Focused on cancer detection using machine learning concepts.",
            "Designed as a research-oriented healthcare application."
        ],
        "link": "#"
    }
]


    for project in project_list:
        with st.container():
            st.subheader(project["title"])
            st.write(project["desc"])
            st.markdown(f"[🔗 View Project]({project['link']})")
            st.markdown("---")

# ---------------- CONTACT ----------------
elif page == "📬 Contact":
    st.header("📬 Get in Touch")
    st.write("I’d love to connect with you!")

    st.markdown("""
    - 📧 Email: g.madhura.tech@gmail.com  
    - 💼 LinkedIn: [Madhura Gundluru](https://www.linkedin.com/in/madhura-gundluru/)  
    - 🐙 GitHub: [madhura276](https://github.com/madhura276)  
    """)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send Message 🚀")






