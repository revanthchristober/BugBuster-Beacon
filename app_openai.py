from openai import OpenAI
import streamlit as st

client = OpenAI(api_key='your_api_key_here')

def get_code_review(code_snippet):
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo-16k-0613',
        messages = [
            {'role': "system", 'content': 'You are a professional code reviewer. Your role is to meticulously review every piece of given code submitted to you, provide detailed feedback on how to improve the code, and offer solutions to fix any issues present. Your feedback should be clear, constructive, and aimed at helping the user write better, more efficient, and error-free code.'},
            {'role': 'user', 'content': f"Review the following code:\n\n{code_snippet}\n\n"}
        ]
    )
    return response.choices[0].message.content


# Streamlit app for code review
def main():
    st.title('BugBuster Beacon - AI Code Reviewer')
    
    # User inputs their code
    code = st.text_area('Enter your code here:', height=300)
    
    if st.button('Review Code'):
        if code:
            # Get the code review from OpenAI API
            review = get_code_review(code)
            st.subheader('Code Review:')
            st.write(review)
        else:
            st.error('Please enter some code to review.')

if __name__ == '__main__':
    main()
