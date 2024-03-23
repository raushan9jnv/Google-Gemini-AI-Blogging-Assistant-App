import streamlit as st

#set app to wide mode
st.set_page_config(layout='wide')

#title of app
st.title('BlogCraft: Your AI Writing Companion')

#create a subheader
st.subheader("Now you can craft perfect blogs with the help of AI- Blogcraft is your new AI blog companion")
blog = '''Artificial intelligence (AI) is changing the way we live and work, and chatbots are playing a significant role in that change. Artificial intelligence has come a long way in recent years, and it’s no surprise that AI chatbots are becoming more and more prevalent in our daily lives. With AI chatbots, we can quickly and easily find answers to our questions, get help with tasks, and even just have a conversation. Two of the most popular AI chatbots out there today are BARD and ChatGPT. Both of these chatbots are designed to make our lives easier, but what are the key differences between them and which one is the best?
        In this blog, we’ll explore the world of AI chatbots and find out what sets BARD and ChatGPT apart from each other.

Outline:
Overview of ChatGPT and BARD
Key differences between ChatGPT and BARD
Concerns with both AI chatbots
Use cases for ChatGPT and BARD
Which one is the best?
Final thoughts
#1. Overview of ChatGPT and BARD:
ChatGPT is a type of artificial intelligence language model that is designed to respond to text-based inputs in a conversational manner. It uses deep learning algorithms to generate responses based on the patterns it has seen in large amounts of text data, and it can be used to build chatbots, answer questions, and perform other language-related tasks.

In simple terms, ChatGPT is like a virtual assistant that can understand and respond to written language. Its goal is to simulate a human-like conversation, allowing users to interact with it in a way that feels natural and intuitive. The technology behind ChatGPT is complex, but the idea is to make it easy for people to use and benefit from it in their daily lives.

You can access ChatGPT from OpenAI official site, click here ChatGPT'''

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

    #submit button
    submit_button = st.button("Generate Blog")

if submit_button:
    st.image("https://avatars.githubusercontent.com/u/86125144?v=4")

    st.write(blog)