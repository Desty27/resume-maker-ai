import streamlit as st
from data_handler import save_user_data
from resume_generator import generate_resume_with_openai

# Translation dictionaries
TRANSLATIONS = {
    'en': {
        'title': "📝 Free Resume Maker",
        'personal': "Personal Details",
        'name': "Full Name*",
        'father': "Father's Name*",
        'village_post': "Village/Post*",
        'landmark': "Near Location",
        'tehsil': "Tehsil",
        'district': "District*",
        'state': "State*",
        'email': "Email",
        'phone': "Phone*",
        'objective': "Career Objective*",
        'education': "Education Details",
        'tenth': "10th Details*",
        'tenth_board': "10th Board*",
        'tenth_year': "10th Passing Year*",
        'tenth_percent': "10th Percentage*",
        'twelfth': "12th Details (Optional)",
        'twelfth_board': "12th Board",
        'twelfth_year': "12th Passing Year",
        'twelfth_percent': "12th Percentage",
        'diploma': "Diploma Details (Optional)",
        'diploma_name': "Diploma Name",
        'diploma_uni': "University",
        'diploma_year': "Passing Year",
        'diploma_percent': "Percentage",
        'project': "Project",
        'training': "Training",
        'submit': "Generate Resume"
    },
    'hi': {
        'title': "📝 रिज्यूम निर्माता",
        'personal': "व्यक्तिगत विवरण",
        'name': "पूरा नाम*",
        'father': "पिता का नाम*",
        'village_post': "गाँव/पोस्ट*",
        'landmark': "निकट स्थान",
        'tehsil': "तहसील",
        'district': "जिला*",
        'state': "राज्य*",
        'email': "ईमेल",
        'phone': "फोन नंबर*",
        'objective': "कैरियर उद्देश्य*",
        'education': "शैक्षिक विवरण",
        'tenth': "10वीं विवरण*",
        'tenth_board': "10वीं बोर्ड*",
        'tenth_year': "10वीं पासिंग वर्ष*",
        'tenth_percent': "10वीं प्रतिशत*",
        'twelfth': "12वीं विवरण (वैकल्पिक)",
        'twelfth_board': "12वीं बोर्ड",
        'twelfth_year': "12वीं पासिंग वर्ष",
        'twelfth_percent': "12वीं प्रतिशत",
        'diploma': "डिप्लोमा विवरण (वैकल्पिक)",
        'diploma_name': "डिप्लोमा नाम",
        'diploma_uni': "विश्वविद्यालय",
        'diploma_year': "पासिंग वर्ष",
        'diploma_percent': "प्रतिशत",
        'project': "प्रोजेक्ट",
        'training': "प्रशिक्षण",
        'submit': "रिज्यूम बनाएं"
    }
}

EDUCATION_OPTIONS = {
    'boards': {
        'en': ["MP Board", "CBSE", "ICSE", "State Board", "Other"],
        'hi': ["एमपी बोर्ड", "सीबीएसई", "आईसीएसई", "राज्य बोर्ड", "अन्य"]
    }
}

def get_translation(lang, key):
    return TRANSLATIONS[lang].get(key, key)

def main():
    st.set_page_config(page_title="Resume Maker", page_icon="📝")
    
    # Language selector
    lang = st.sidebar.selectbox("भाषा/ Language", ["en", "hi"])
    
    st.title(get_translation(lang, 'title'))
    
    with st.form("resume_form"):
        # Personal Information
        st.header(get_translation(lang, 'personal'))
        name = st.text_input(get_translation(lang, 'name'), placeholder="Rahul Sharma" if lang == 'en' else "राहुल शर्मा")
        father_name = st.text_input(get_translation(lang, 'father'), placeholder="Ravi Sharma" if lang == 'en' else "रवि शर्मा")
        
        # Address Details
        village_post = st.text_input(get_translation(lang, 'village_post'), placeholder="Khor" if lang == 'en' else "खोर")
        landmark = st.text_input(get_translation(lang, 'landmark'), placeholder="Near Indra Colony" if lang == 'en' else "इंद्रा कॉलोनी के पास")
        tehsil = st.text_input(get_translation(lang, 'tehsil'), placeholder="Jawad" if lang == 'en' else "जावद")
        
        col1, col2 = st.columns(2)
        with col1:
            district = st.text_input(get_translation(lang, 'district'), placeholder="Neemuch" if lang == 'en' else "नीमच")
        with col2:
            state = st.text_input(get_translation(lang, 'state'), placeholder="Madhya Pradesh" if lang == 'en' else "मध्य प्रदेश")
        
        email = st.text_input(get_translation(lang, 'email'), placeholder="example@email.com")
        phone = st.text_input(get_translation(lang, 'phone'), placeholder="9876543210")

        # Career Objective
        st.header(get_translation(lang, 'objective'))
        objective = st.text_area(get_translation(lang, 'objective'), height=100,
                               placeholder="To achieve a challenging position..." if lang == 'en' else "उद्योग में एक चुनौतीपूर्ण स्थान प्राप्त करने के लिए...")

        # Education Details
        st.header(get_translation(lang, 'education'))
        
        # Compulsory 10th details
        st.subheader(get_translation(lang, 'tenth'))
        col1, col2, col3 = st.columns(3)
        with col1:
            tenth_board = st.selectbox(get_translation(lang, 'tenth_board'), EDUCATION_OPTIONS['boards'][lang])
        with col2:
            tenth_year = st.number_input(get_translation(lang, 'tenth_year'), 1990, 2024, 2010)
        with col3:
            tenth_percent = st.number_input(get_translation(lang, 'tenth_percent'), 0.0, 100.0, 60.0)

        # Optional 12th details
        st.subheader(get_translation(lang, 'twelfth'))
        add_twelfth = st.checkbox(get_translation(lang, 'twelfth').split(" (")[0])
        if add_twelfth:
            col1, col2, col3 = st.columns(3)
            with col1:
                twelfth_board = st.selectbox(get_translation(lang, 'twelfth_board'), EDUCATION_OPTIONS['boards'][lang])
            with col2:
                twelfth_year = st.number_input(get_translation(lang, 'twelfth_year'), 1990, 2024, 2012)
            with col3:
                twelfth_percent = st.number_input(get_translation(lang, 'twelfth_percent'), 0.0, 100.0, 60.0)

        # Optional Diploma details
        st.subheader(get_translation(lang, 'diploma'))
        add_diploma = st.checkbox(get_translation(lang, 'diploma').split(" (")[0])
        if add_diploma:
            diploma_name = st.text_input(get_translation(lang, 'diploma_name'), placeholder="Diploma in Mechanical Engineering" if lang == 'en' else "मैकेनिकल इंजीनियरिंग में डिप्लोमा")
            university = st.text_input(get_translation(lang, 'diploma_uni'), placeholder="RGPV Bhopal" if lang == 'en' else "आरजीपीवी भोपाल")
            col1, col2 = st.columns(2)
            with col1:
                diploma_year = st.number_input(get_translation(lang, 'diploma_year'), 1990, 2024, 2015)
            with col2:
                diploma_percent = st.number_input(get_translation(lang, 'diploma_percent'), 0.0, 100.0, 65.0)

        # Project and Training
        st.header(get_translation(lang, 'project'))
        project = st.text_input(get_translation(lang, 'project'), placeholder="Regenerative Braking System" if lang == 'en' else "रीजनरेटिव ब्रेकिंग सिस्टम")

        st.header(get_translation(lang, 'training'))
        training = st.text_input(get_translation(lang, 'training'), placeholder="Industrial Training" if lang == 'en' else "औद्योगिक प्रशिक्षण")

        submitted = st.form_submit_button(get_translation(lang, 'submit'))

    if submitted:
        # Prepare education data
        education_data = {
            'tenth': {
                'board': tenth_board,
                'year': tenth_year,
                'percent': tenth_percent
            }
        }
        
        if add_twelfth:
            education_data['twelfth'] = {
                'board': twelfth_board,
                'year': twelfth_year,
                'percent': twelfth_percent
            }

        # Prepare technical data
        technical_data = {}
        if add_diploma:
            technical_data['diploma'] = {
                'name': diploma_name,
                'university': university,
                'year': diploma_year,
                'percent': diploma_percent
            }

        user_data = {
            "personal": {
                "name": name,
                "father_name": father_name,
                "address": {
                    "village_post": village_post,
                    "landmark": landmark,
                    "tehsil": tehsil,
                    "district": district,
                    "state": state
                },
                "contact": {
                    "email": email,
                    "phone": phone
                }
            },
            "objective": objective,
            "education": education_data,
            "technical": technical_data,
            "project": project,
            "training": training
        }

        save_user_data(user_data)
        
        with st.spinner("Generating resume..." if lang == 'en' else "रिज्यूम बनाया जा रहा है..."):
            html_content = generate_resume_with_openai(user_data, st.secrets["OPENAI_API_KEY"])
        
        if html_content:
            st.success("Resume generated!" if lang == 'en' else "रिज्यूम तैयार है!")
            st.download_button(
                label="Download" if lang == 'en' else "डाउनलोड करें",
                data=html_content,
                file_name=f"{name}_Resume.html",
                mime="text/html"
            )

if __name__ == "__main__":
    main()