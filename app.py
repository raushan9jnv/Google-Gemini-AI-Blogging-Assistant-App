import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

# Set up the model
genai.configure(api_key= google_gemini_api_key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#setting up our model
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

#set app to wide mode
st.set_page_config(layout='wide')

#title of app
st.title('BlogCraft: Your AI Writing Companion')

#create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI- Blogcraft is your new AI blog companion")

#sidebar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of Blog You want to generate")

    #blog title
    blog_title = st.text_input("Blog Title")

    #keywords input
    keywords = st.text_area("Keywords (comma-seperated)")

    #Number of words
    num_words = st.slider("Number of Words", min_value = 250, max_value= 1000, step= 250)

    #Number of images
    num_images = st.number_input("Number of Images", min_value=0, max_value=5,step=1)

    prompt_parts= [
        f"generate a comprehensivee, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\". make sure to incorporate these keywords in the blog post. the blog should be approximately {num_words} words in length, suitable for an online audience. ensure the content is original, informative, and maintains a consist tone throughout."]

    response = model.generate_content(prompt_parts)
    #submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    # st.image("https://avatars.githubusercontent.com/u/86125144?v=4")

    st.write(response.text)