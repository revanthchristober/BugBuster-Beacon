import streamlit as st
import google.generativeai as genai

# Configure the Gemini API
GOOGLE_API_KEY = 'your_api_key_here'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.title("BugBuster Beacon - AI Code Reviewer")
    code = st.text_area("Enter your Python code for review:", height=200)
    
    if st.button("Review Code"):
        response = model.generate_content(f"This Python code snippet potentially contains bugs or areas for improvement:\n\n```python\n{code}\n```\nPlease identify potential issues and suggest fixes, including code snippets demonstrating the improvements.")
        
        st.subheader("Review Results:")
        st.write(response.text)

if __name__ == "__main__":
    main()
