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
    with open("Madhura_G.pdf", "rb") as file:  # Make sure file is in same folder
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
        st.write("- Python\n- JavaScript\n- HTML, CSS")

        st.subheader("Data Science & ML/AI")
        st.write("""
        - Data Analysis: Pandas, NumPy  
        - Machine Learning & Deep Learning: Scikit-learn, TensorFlow  
        - Image Classification, NLP  
        """)

    with col2:
        st.subheader("Tools & Platforms")
        st.write("- Streamlit\n- Power BI, Excel\n- GitHub")

        st.subheader("Soft Skills")
        st.write("""
        - Time Management  
        - Adaptability
        """)

# ---------------- PROJECTS ----------------
elif page == "📂 Projects":
    st.header("📂 Projects Showcase")

    project_list = [
        {
            "title": "📊 SMS Spam Detection",
            "desc": "A Machine Learning project using NLP to classify messages as Spam or Not Spam.",
            "link": "https://github.com/madhura276/SMS-Spam-Detection"
        },
        {
            "title": "🎓 Student Score Manager",
            "desc": "A Python file-handling project to manage and analyze student scores.",
            "link": "https://github.com/madhura276/student-management-system"
        },
        {
            "title": "🩺 Cervical Cancer Detection",
            "desc": "AI-driven academic project using research papers for cancer detection.",
            "link": "#"
        },
        {
            "title": "📈 Data Analysis with Pandas & NumPy",
            "desc": "Analyzed datasets for cleaning, transformation, and insights.",
            "link": "https://github.com/madhura276/Netflix_Data_Analysis"
        },
        {
            "title": "🛒 Online Shopping Cart",
            "desc": "Built a shopping cart system with product listing, cart updates, and checkout simulation.",
            "link": "https://github.com/madhura276/Online-Shopping-Cart"
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
