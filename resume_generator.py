import openai

def generate_resume_with_openai(user_data, api_key):
    """Generate enhanced resume content using OpenAI API"""
    openai.api_key = api_key
    
    prompt = f"""
    Create a professional resume in HTML format for a rural Indian student using this data:
    {user_data}

    Add these enhancements:
    1. Infer and add relevant achievements from projects/experience
    2. Suggest appropriate skill descriptions
    3. Add missing but relevant sections (like Objectives if empty)
    4. Include industry-appropriate terminology for their education stream
    5. Add relevant coursework/projects based on their skills
    6. Suggest measurable accomplishments where possible
    7. Add professional summary if missing

    Formatting requirements:
    - Use clean HTML with inline CSS
    - Highlight enhancements with 'AI-suggested' comments
    - Maintain original user content
    - Make sections for: Summary, Education, Skills, Experience, Projects, Certifications

    Return ONLY the HTML code without any markdown.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """You are a career counselor helping rural students. 
                Enhance resumes by:
                - Adding relevant missing information
                - Expanding brief descriptions
                - Suggesting measurable achievements
                - Using appropriate industry terms"""},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"OpenAI API Error: {str(e)}")