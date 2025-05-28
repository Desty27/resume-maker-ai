# resume_generator.py
import openai

def generate_resume_with_openai(user_data, api_key):
    """Generate resume content using OpenAI API with strict formatting"""
    openai.api_key = api_key
    
    prompt = f"""
    
    Create a professional resume in HTML format strictly following this structure:
    [Personal Details]
    Name in bold
    Address format:
    Vill/Post: [village]
    Near [landmark], [tehsil]
    Distt.: [district]
    Email: [email]
    Contact No.: [phone]
    
    [Career Objective]
    Single paragraph
    
    [Educational Qualification]
    Table with columns: Qualification | Board/University | Year of Passing | Percentage
    - 10th
    - 12th (if available)
    
    [Technical Qualification]
    Table with columns: Qualification | University | Year of Passing | Percentage
    - Diploma (if available)
    
    [Project]
    - [project details]
    
    [Training]
    - [training details]
    
    User Data:
    {user_data}
    
    Enhancements Needed:
    1. Expand brief project descriptions with technical specifications
    2. Add relevant industry keywords to career objective
    3. Format percentages consistently (XX.XX%)
    4. Add missing contact information formatting
    5. Include relevant technical skills in project/training
    
    Required Format:
    - Use HTML tables with border="1" cellpadding="5"
    - Maintain exact section order and headings
    - Use <sup>th</sup> for qualification levels
    - Bold section headings using <b> tags
    - No CSS styling
    
    Return ONLY the HTML code without any additional text.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a technical resume formatter that maintains exact structure while enhancing content"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"OpenAI API Error: {str(e)}")