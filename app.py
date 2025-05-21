import streamlit as st
from data_handler import save_user_data
from resume_generator import generate_resume_with_openai

def main():
    st.set_page_config(page_title="Free Resume Maker", page_icon="📝")
    
    st.title(" Free Resume Maker for Students")
    st.markdown("Answer simple questions to create your resume")

    # Check for API key
    if 'OPENAI_API_KEY' not in st.secrets:
        st.warning("Please configure your OpenAI API key in Streamlit secrets")
        return

    with st.form("resume_form"):
        # Personal Information
        st.header("1. Personal Details")
        name = st.text_input("Full Name*", placeholder="Rahul Sharma")
        father_name = st.text_input("Father's Name*", placeholder="Ravi Sharma")
        dob = st.date_input("Date of Birth*")
        gender = st.selectbox("Gender*", ["Male", "Female", "Other"])
        
        col1, col2 = st.columns(2)
        with col1:
            state = st.selectbox("State*", [
                "Odisha", "Bihar", "Madhya Pradesh", 
                "Rajasthan", "Chhattisgarh", "Other"
            ])
        with col2:
            district = st.text_input("District*", placeholder="Your district")
        
        village = st.text_input("Village/Town*", placeholder="Your village/town")
        whatsapp = st.text_input("WhatsApp Number*", placeholder="9876543210")
        email = st.text_input("Email (if available)", placeholder="(optional)")

        # Education Details
        st.header("2. Education")
        education_level = st.selectbox("Highest Education*", 
                                    ["10th Pass", "12th Pass", "Diploma"])
        
        school_name = st.text_input("School/College Name*", placeholder="Government High School")
        board = st.selectbox("Board*", 
                           ["Odisha Board", "Bihar Board", "CBSE", "ICSE", "State Board", "Other"])
        passing_year = st.selectbox("Passing Year*", list(range(2010, 2024))[::-1])
        
        if education_level in ["12th Pass", "Diploma"]:
            stream = st.selectbox("Stream/Subject", 
                                ["Science", "Commerce", "Arts", "Vocational", "Engineering", "Other"])

        # Skills
        st.header("3. Skills")
        skills = st.multiselect("What skills do you have?", [
            "Basic Computer Knowledge",
            "MS Office",
            "Internet Browsing",
            "Typing",
            "English Speaking",
            "Hindi Speaking",
            "Mathematics",
            "Farming Knowledge",
            "Machine Operation"
        ])

        # Experience
        st.header("4. Experience")
        experience_type = st.selectbox("Any experience?", [
            "No experience",
            "Internship",
            "Part-time work",
            "Helped in family business",
            "Social work",
            "Project work"
        ])

        if experience_type != "No experience":
            exp_description = st.text_area("Describe your experience", 
                                         placeholder="Example: 3 months internship at...")

        # Projects
        st.header("5. Projects")
        project_name = st.text_input("Any school projects or special work?", placeholder="Example: Science project...")
        
        # Languages
        st.header("6. Languages")
        languages = st.multiselect("Which languages do you know?", 
                                 ["Hindi", "English", "Odia", "Urdu", "Local language"])

        submitted = st.form_submit_button("Generate Resume with AI")

    if submitted:
        # Validate required fields
        required_fields = [name, father_name, dob, gender, state, district, village, whatsapp, education_level, school_name, board, passing_year]
        if not all(required_fields):
            st.error("Please fill all required fields (marked with *)")
            return

        # Prepare data
        user_data = {
            "personal": {
                "name": name,
                "father_name": father_name,
                "dob": str(dob),
                "gender": gender,
                "state": state,
                "district": district,
                "village": village,
                "whatsapp": whatsapp,
                "email": email if email else ""
            },
            "education": {
                "level": education_level,
                "school": school_name,
                "board": board,
                "year": passing_year,
                "stream": stream if education_level in ["12th Pass", "Diploma"] else ""
            },
            "skills": skills,
            "experience": {
                "type": experience_type,
                "description": exp_description if experience_type != "No experience" else ""
            },
            "project": project_name if project_name else "",
            "languages": languages
        }

        save_user_data(user_data)
        
        with st.spinner("Generating professional resume with AI..."):
            html_content = generate_resume_with_openai(
                user_data, 
                st.secrets["OPENAI_API_KEY"]
            )
        
        if html_content:
            st.success("Your AI-generated resume is ready!")
            st.balloons()
            
            st.subheader("Preview")
            st.components.v1.html(html_content, height=800, scrolling=True)
            
            st.download_button(
                label=" Download Resume",
                data=html_content,
                file_name=f"{name}_Resume.html",
                mime="text/html"
            )

if __name__ == "__main__":
    main() 