import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import base64

# Function to get base64 of image
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set page config
st.set_page_config(
    page_title="Career Builders' International Schools",
    page_icon="logo.JPG",
    layout="wide"
)

# Get background image base64
background_image = get_base64_of_bin_file("groupstage.PNG")

# Custom CSS with updated styles
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: #2C3E50 !important;
        font-weight: 600;
    }
    
    /* Main container */
    .main {
        padding: 2rem;
        background-color: #F8F9FA;
    }
    
    /* Content wrapper */
    .stApp > div > div > div > div > div {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #ffffff;  /* Pure white */
    }
    
    /* School section cards */
    .school-section {
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        background-color: #ffffff;  /* Pure white */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);  /* Subtle shadow */
        border: 1px solid #f0f0f0;  /* Light gray border */
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #2C3E50 !important;
        color: #FFFFFF !important;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 700 !important;  /* Made text bolder */
        border: none;
        transition: all 0.3s ease;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;  /* Added text shadow */
        letter-spacing: 0.5px !important;  /* Added letter spacing */
        font-size: 1.1rem !important;  /* Slightly larger font */
    }
    
    .stButton>button:hover {
        background-color: #34495E !important;
        box-shadow: 0 2px 4px rgba(44, 62, 80, 0.1);
        color: #FFFFFF !important;  /* Ensure text stays white on hover */
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;  /* Stronger shadow on hover */
    }
    
    /* Form elements */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
    }
    
    .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
    }
    
    /* Dataframes */
    .dataframe {
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        background-color: #ffffff;
        border: 1px solid #f0f0f0;
    }
    
    /* Metrics */
    .stMetric {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #f0f0f0;
    }
    
    /* Radio buttons in sidebar */
    .stRadio>div {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        border: 1px solid #f0f0f0;
    }
    
    /* Links */
    a {
        color: #e75480;  /* Pink */
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: #ff69b4;  /* Hot pink */
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f5f5f5;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #e75480;  /* Pink */
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #ff69b4;  /* Hot pink */
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #ffffff;
        border: 1px solid #e75480;  /* Pink border */
        color: #e75480;  /* Pink text */
    }
    
    /* File uploader */
    .stFileUploader>div {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
    }
    
    /* Logo styling */
    .sidebar-logo {
        width: 100%;
        max-width: 200px;
        margin: 0 auto;
        display: block;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* School motto styling */
    .school-motto {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        color: #2C3E50;
        text-align: center;
        font-size: 1.3em;
        margin: 1.5rem 0;
        padding: 1.2rem;
        border: 2px solid #E9ECEF;
        border-radius: 12px;
        background-color: #FFFFFF;
    }
    
    /* Navigation buttons styling */
    .nav-button {
        background-color: #ffffff;
        border: 2px solid #e75480;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        color: #e75480;
    }
    
    .nav-button:hover {
        background-color: #e75480;
        color: white;
        transform: translateY(-5px);
        box-shadow: 0 4px 8px rgba(231, 84, 128, 0.2);
    }
    
    .nav-button i {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .nav-button h3 {
        margin: 0;
        font-size: 1.5rem;
    }
    
    .nav-button p {
        margin: 0.5rem 0 0;
        font-size: 1rem;
        opacity: 0.8;
    }
    
    /* Back to Home button styling */
    .back-home-button {
        background-color: #2C3E50 !important;
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;  /* Made text bolder */
        padding: 0.75rem 1.5rem !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0 2px 4px rgba(44, 62, 80, 0.1) !important;
        margin: 1rem 0 2rem 0 !important;
        width: 100% !important;
        max-width: 250px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        transition: all 0.3s ease !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;  /* Added text shadow */
        letter-spacing: 0.5px !important;  /* Added letter spacing */
    }
    
    .back-home-button:hover {
        background-color: #34495E !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 6px rgba(44, 62, 80, 0.15) !important;
        color: #FFFFFF !important;  /* Ensure text stays white on hover */
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;  /* Stronger shadow on hover */
    }
    
    .back-home-button:active {
        transform: translateY(0) !important;
    }
    
    /* Container for back button to make it sticky */
    .back-button-container {
        position: fixed !important;
        top: 20px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        z-index: 999 !important;
        background-color: rgba(255, 255, 255, 0.95) !important;
        padding: 8px !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 4px rgba(44, 62, 80, 0.1) !important;
        width: auto !important;
        min-width: 180px !important;
        max-width: 250px !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid #E9ECEF !important;
    }
    
    /* Add padding to the main content to prevent overlap with sticky button */
    .main .block-container {
        padding-top: 80px !important;
    }
    
    /* Contact info styling */
    .contact-info {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(44, 62, 80, 0.1);
        margin: 1rem 0;
        border: 1px solid #E9ECEF;
    }
    
    .contact-info h3 {
        color: #2C3E50;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .contact-info p {
        font-size: 1.1rem;
        margin: 0.5rem 0;
        color: #495057;
    }
    
    /* Flyer section styling */
    .flyer-section {
        background-color: #FFFFFF;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(44, 62, 80, 0.1);
        margin: 2rem 0;
        border: 1px solid #E9ECEF;
    }
    
    .flyer-section h3 {
        color: #2C3E50;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    /* Make text more readable */
    p, li, .stMarkdown {
        color: #495057;
        font-weight: 400;
        line-height: 1.6;
    }
    
    /* Navigation buttons in grid */
    .nav-grid .stButton>button {
        height: 120px !important;
        font-size: 1.3rem !important;  /* Larger font for nav buttons */
        font-weight: 700 !important;  /* Made text bolder */
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2) !important;  /* Added text shadow */
        letter-spacing: 0.5px !important;  /* Added letter spacing */
    }
    
    .nav-grid .stButton>button:hover {
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;  /* Stronger shadow on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for navigation if it doesn't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Header
st.title("CAREER BUILDERS INTERNATIONAL SCHOOL")
st.markdown("### 43/44 UMUOLA ROAD BY BOURDEX AVENUE OGBOR HILL, ABA")
st.markdown('<div class="school-motto">Excellence in Education, Character, and Innovation</div>', unsafe_allow_html=True)

# Sidebar with just logo and contact info
with st.sidebar:
    st.image("logo.JPG", caption="Career Builders' Logo", use_container_width=True)
    st.markdown("---")
    st.markdown("### Contact Information")
    st.write("📞 Phone: +234 803 763 4201")
    st.write("📞 Phone: +234 803 711 0826")
    st.write("📧 Email: careerbuildersinternationalsch@gmail.com")
    st.write("📍 Address: 43/44 Umuola Road by Bourdex Avenue, Ogbor Hill, Aba")
    st.markdown("---")
    st.markdown("### Academic Examinations")
    st.write("""
    We undertake the following examinations:
    • First School Leaving Exams
    • Common Entrance Exam
    • Junior WAEC
    • WAEC
    • NECO
    """)

# Navigation buttons in 2x2 grid
if st.session_state.current_page == "Home":
    st.markdown("## Welcome to Career Builders International Schools, Aba")
    st.write("""
    We offer quality education from Crèche to Secondary level. With qualified teachers, 
    modern labs, and a secure CCTV-surveilled campus, we nurture future leaders with 
    integrity, knowledge, and confidence.
    """)
    
    # Two-column layout for programs and achievement
    col1, col2 = st.columns([1, 1.2])  # Made the achievement column slightly wider
    
    with col1:
        st.markdown("### 📚 Our Academic Programs")
        programs = {
            "Level": ["Crèche", "Pre-Nursery", "Nursery", "Primary", "Secondary"],
            "Status": ["Admission Open", "Admission Open", "Admission Open", "Admission Open", "Admission Open"]
        }
        st.dataframe(pd.DataFrame(programs), hide_index=True)
        st.markdown("""
        *We offer a comprehensive educational journey from early childhood through secondary education, 
        with a focus on academic excellence and character development.*
        """)
    
    with col2:
        st.markdown("### 🏆 Student Achievement")
        st.markdown("#### First Position in Spelling Bee Competition")
        st.video("crunches awarding carrer builder student 1st position spelling bee.MP4")
        st.markdown("""
        *Our student's outstanding achievement in the spelling bee competition demonstrates 
        our commitment to academic excellence and student development. This success reflects 
        the quality of education and support we provide at Career Builders International Schools.*
        """)

    # Download Flyer Section
    st.markdown("---")
    st.markdown("### 📄 School Information Flyer")
    flyer_col1, flyer_col2 = st.columns([1, 2])
    with flyer_col1:
        st.image("downloadable flyer.JPG", caption="School Information Flyer", use_container_width=True)
    with flyer_col2:
        st.markdown("""
        Download our comprehensive school information flyer to learn more about:
        - Our academic programs
        - Admission requirements
        - School facilities
        - Contact information
        - And much more!
        """)
        with open("downloadable flyer.JPG", "rb") as file:
            btn = st.download_button(
                label="📥 Download School Flyer",
                data=file,
                file_name="Career_Builders_International_School_Flyer.jpg",
                mime="image/jpeg",
                use_container_width=True
            )

    # Navigation buttons in 2x2 grid
    st.markdown("## Explore Our School")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("About Us", key="about_btn", use_container_width=True):
            st.session_state.current_page = "About Us"
            st.rerun()
        if st.button("Admissions", key="admissions_btn", use_container_width=True):
            st.session_state.current_page = "Admissions"
            st.rerun()
    with col2:
        if st.button("Extracurricular Activities", key="activities_btn", use_container_width=True):
            st.session_state.current_page = "Activities"
            st.rerun()
        if st.button("Contact Us", key="contact_btn", use_container_width=True):
            st.session_state.current_page = "Contact"
            st.rerun()

    # Key Features
    st.markdown("## Our Facilities")
    features = {
        "Facility": [
            "Science Laboratory",
            "Computer Laboratory",
            "Library",
            "Security System",
            "Learning Environment"
        ],
        "Description": [
            "State-of-the-art equipment for practical learning",
            "Modern computer facilities for digital education",
            "Well-stocked with up-to-date learning materials",
            "CCTV-enabled for active surveillance",
            "Conducive environment for learning and co-curricular activities"
        ]
    }
    st.dataframe(pd.DataFrame(features), hide_index=True)

# Add a back to home button only when not on home page
if st.session_state.current_page != "Home":
    st.markdown('<div class="back-button-container">', unsafe_allow_html=True)
    if st.button("← Back to Home", key="back_btn", use_container_width=True):
        st.session_state.current_page = "Home"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Main content based on current page
if st.session_state.current_page == "About Us":
    st.markdown("## Our History")
    st.write("""
    Career Builders' International Schools started as a single primary institution and has 
    grown by leaps and bounds into what can be described today as a string of Citadels with 
    state-of-the-art innovations. Our journey began in 2012 under the giant and visionary 
    strides of Sir Basil and Lady Mrs Stella Okolo.
    """)
    
    st.markdown("### Our Mission")
    st.write("""
    We are committed to nurturing and fostering sustainable and standard education with a 
    view to developing an all-round cum Montessori-based learning system in a society fast 
    eroding from core academic values and moral fibre.
    """)
    
    st.markdown("### Academic Excellence")
    st.write("""
    Our school's motto, imbued on deep academic excellence and progress, attests to the fact 
    that our numerous academic records are quite exceptional and simply unequalled. Our 
    students are well-groomed under high and strict moral discipline, in line with global 
    best practices, courtesy of our team of skilled, result-driven, and God-fearing teachers.
    """)
    
    st.markdown("### Our Facilities")
    st.write("""
    At Career Builders', our facilities are top-notch and second to none, featuring:
    - World-class equipment in science and computer laboratories
    - Well-stocked library with up-to-date learning materials
    - CCTV-enabled for active surveillance
    - Conducive environment for learning and co-curricular activities
    """)

elif st.session_state.current_page == "Activities":
    st.markdown("## Extracurricular Activities 🎭")
    
    # Video Gallery
    st.markdown("### Our Activities Gallery")
    
    # Create columns for video grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Cultural Day Celebration")
        st.video("cultural day.MP4")
        st.markdown("""
        *Experience the vibrant celebration of our Cultural Day, where students showcase 
        the rich diversity of Nigerian culture through traditional dances, music, and 
        cultural displays. This event promotes cultural awareness and unity among our students.*
        """)
        
        st.markdown("#### Cultural Day Celebration (Part 2)")
        st.video("cultural day 2 .MP4")
        st.markdown("""
        *Continuing our Cultural Day festivities, this video captures more cultural 
        performances and activities, highlighting the creativity and cultural pride of 
        our students. Watch as they bring traditional customs to life through engaging 
        presentations and performances.*
        """)
        
        st.markdown("#### Students on Assembly Ground")
        st.video("students on assembly ground.MP4")
        st.markdown("""
        *A glimpse into our daily morning assembly routine, where students gather for 
        prayers, announcements, and morning exercises. This daily practice instills 
        discipline, unity, and a sense of community among our students.*
        """)
    
    with col2:
        st.markdown("#### Question and Answer Session")
        st.video("question and answer by students.MP4")
        st.markdown("""
        *Watch our students engage in an interactive question and answer session, 
        demonstrating their critical thinking skills and knowledge. These sessions 
        encourage active participation, boost confidence, and enhance learning through 
        peer interaction.*
        """)
        
        st.markdown("#### Students Exercising")
        st.video("students execersing in assembly ground.MP4")
        st.markdown("""
        *Our students participate in physical exercises during assembly, promoting 
        physical fitness and healthy habits. These daily exercise routines help 
        students stay active, focused, and ready for the day's learning activities.*
        """)
    
    # Activities Description
    st.markdown("### Our Activities Program")
    st.write("""
    At Career Builders International Schools, we believe in holistic education. Our 
    extracurricular activities are designed to develop well-rounded individuals through:
    
    - Cultural and Arts Programs
    - Sports and Physical Education
    - Science and Technology Exhibitions
    - Annual Prize Giving Ceremonies
    - Leadership Development Programs
    - Debate and Public Speaking
    - Music and Dance Performances
    - Morning Assembly Activities
    - Interactive Learning Sessions
    """)
    
    # Schedule
    st.markdown("### Activities Schedule")
    schedule = {
        "Activity": [
            "Morning Assembly",
            "Cultural Day",
            "Exercise Sessions",
            "Interactive Learning",
            "Sports Day",
            "Prize Giving Day"
        ],
        "Frequency": [
            "Daily",
            "Annually",
            "Daily",
            "Weekly",
            "Termly",
            "Annually"
        ],
        "Description": [
            "Morning assembly with exercises and announcements",
            "Cultural celebration and performances",
            "Physical education and exercise routines",
            "Student-led question and answer sessions",
            "Inter-house sports competition",
            "Academic excellence recognition"
        ]
    }
    st.dataframe(pd.DataFrame(schedule), hide_index=True)

elif st.session_state.current_page == "Admissions":
    st.markdown("## Admissions Process 📝")
    st.write("""
    Join our community of learners at Career Builders International Schools. We welcome 
    students who are committed to academic excellence and personal growth. Our comprehensive 
    educational program spans from early childhood through secondary education, ensuring 
    a seamless learning journey for every student.
    """)
    
    # Educational Levels Information
    st.markdown("### Our Educational Programs")
    
    # Crèche Section
    st.markdown("#### 👶 Crèche Program (Ages 0-2)")
    st.markdown("""
    Our crèche program provides a nurturing and safe environment for our youngest learners:
    - Professional caregivers with specialized training in early childhood development
    - Age-appropriate activities and learning materials
    - Safe, clean, and stimulating environment
    - Regular health monitoring and care
    - Nutritious meals and snacks
    - Daily communication with parents
    - Focus on early motor skills and social development
    """)
    
    # Pre-Nursery Section
    st.markdown("#### 🎨 Pre-Nursery Program (Ages 2-3)")
    st.markdown("""
    Our pre-nursery program focuses on early learning and development:
    - Montessori-based learning approach
    - Introduction to basic concepts through play
    - Development of social skills and independence
    - Creative arts and music activities
    - Early language development
    - Basic numeracy skills
    - Physical development through structured play
    """)
    
    # Nursery Section
    st.markdown("#### 🎯 Nursery Program (Ages 3-5)")
    st.markdown("""
    Our nursery program prepares children for primary education:
    - Structured learning environment
    - Introduction to reading and writing
    - Basic mathematics and science concepts
    - Social and emotional development
    - Creative expression through arts
    - Physical education and sports
    - Computer literacy basics
    - Character building and moral values
    """)
    
    # Primary Section
    st.markdown("#### 📚 Primary Education (Ages 5-11)")
    st.markdown("""
    Our primary education program provides a strong academic foundation:
    - Comprehensive curriculum aligned with national standards
    - Experienced and qualified teachers
    - Small class sizes for personalized attention
    - Regular assessments and progress tracking
    - Extracurricular activities and sports
    - Computer and technology integration
    - Preparation for Common Entrance Examination
    - Character education and leadership development
    """)
    
    # Secondary Section
    st.markdown("#### 🎓 Secondary Education (Ages 11-17)")
    st.markdown("""
    Our secondary education program prepares students for higher education and future careers:
    - WEAC and NECO approved curriculum
    - Specialized subject teachers
    - State-of-the-art science and computer laboratories
    - Comprehensive examination preparation
    - Career guidance and counseling
    - Leadership and character development
    - Sports and extracurricular activities
    - University and career preparation
    """)
    
    # Common Features
    st.markdown("### Our Commitment to Excellence")
    st.markdown("""
    Across all levels, we maintain the highest standards of education:
    
    **Academic Excellence**
    - Qualified and experienced teachers
    - Modern teaching methods and resources
    - Regular assessments and progress tracking
    - Individual attention to students
    
    **Facilities**
    - Well-equipped classrooms
    - Modern science and computer laboratories
    - Well-stocked library
    - Sports facilities
    - CCTV surveillance for security
    
    **Student Support**
    - Regular parent-teacher communication
    - Counseling services
    - Health monitoring
    - Extracurricular activities
    - Character development programs
    
    **Safety and Security**
    - 24/7 CCTV surveillance
    - Secure campus environment
    - Regular safety drills
    - Qualified security personnel
    """)
    
    # Contact for Admission
    st.markdown("### 📞 For Admission Inquiries")
    st.markdown("""
    **Contact us directly for admission information and procedures:**
    
    📞 Phone: +234 803 763 4201  
    📞 Phone: +234 803 711 0826  
    📧 Email: careerbuildersinternationalsch@gmail.com  
    📍 Visit: 43/44 Umuola Road by Bourdex Avenue, Ogbor Hill, Aba
    """)

elif st.session_state.current_page == "Contact":
    st.markdown("## Contact Us 📞")
    
    # Contact Information with enhanced styling
    st.markdown("""
    <style>
    .contact-info {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border: 2px solid #e75480;
    }
    .contact-info h3 {
        color: #e75480;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .contact-info p {
        font-size: 1.2rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Contact Information in a styled container
    st.markdown('<div class="contact-info">', unsafe_allow_html=True)
    st.markdown("### 📍 School Location")
    st.markdown("""
    **Career Builders International School**  
    43/44 Umuola Road by Bourdex Avenue  
    Ogbor Hill, Aba
    """)
    
    st.markdown("### 📞 Contact Details")
    st.markdown("""
    **Phone:** +234 803 763 4201  
    **Phone:** +234 803 711 0826  
    **Email:** careerbuildersinternationalsch@gmail.com
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Download Flyer Section with enhanced styling
    st.markdown("""
    <style>
    .flyer-section {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 2rem 0;
        border: 2px solid #e75480;
    }
    .flyer-section h3 {
        color: #e75480;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="flyer-section">', unsafe_allow_html=True)
    st.markdown("### 📄 Download School Information")
    flyer_col1, flyer_col2 = st.columns([1, 2])
    with flyer_col1:
        st.image("downloadable flyer.JPG", caption="School Information Flyer", use_container_width=True)
    with flyer_col2:
        st.markdown("""
        **Download our comprehensive school information flyer to learn more about:**
        - Our academic programs
        - Admission requirements
        - School facilities
        - Contact information
        - And much more!
        """)
        with open("downloadable flyer.JPG", "rb") as file:
            btn = st.download_button(
                label="📥 Download School Flyer",
                data=file,
                file_name="Career_Builders_International_School_Flyer.jpg",
                mime="image/jpeg",
                use_container_width=True
            )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Map placeholder
    st.markdown("### 📍 Location Map")
    st.write("📍 43/44 Umuola Road by Bourdex Avenue, Ogbor Hill, Aba")
    # Note: You can add an actual map using streamlit's map feature or an iframe 