import os
import openai
from dotenv import load_dotenv

load_dotenv()
SAMBANOVA_API_KEY = os.environ.get("SAMBANOVA_API_KEY")
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def groq_call(user_input, df, model_name):
    print("model_name", model_name)
    client = Groq(api_key=GROQ_API_KEY)
    prompt =f"A dataset contains these columns: {df.columns.tolist()} \
            python code to do the following : {user_input}. Tips: Use matplotlib library to create the plot and assume I already have the library installed. \
            only givem me the code else I  will kill someone if you give extra information or anything else. \
            Please write ALL the code needed since it will be extracted directly and run from your response.\
            Always have the csv file name to be 'dataset.csv'\
            Always start the code with '''python and end with '''"
    print("prompt", prompt)
    # prompt =f" TASK:Python programming language code to generate plots from given csv file info. A dataset contains these columns: {df.columns.tolist()} \
    #     python code to do the following : {user_input}. Tips: Use matplotlib library to create the plot and assume I already have the library installed. \
    #     only give me the python code. \
    #     Please write ALL the code needed since it will be extracted directly and run from your response.\
    #     Always have the csv file name to be 'dataset.csv'\
    #     Only code, no other text or comments. \
    #     Always start the code with '''python and end with '''"
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        # model="llama3-b-8192",
        model=model_name
    )
    text = chat_completion.choices[0].message.content
    return text, prompt

def call_snova(user_input, df, model_name):
    # print("model_name", model_name)
    # print("user_input", user_input)
    # print("df", df.columns.tolist())
    prompt =f"""A dataset contains these columns: {df.columns.tolist()} \
        python code to do the following : {user_input}.
        only give me the code else I  will kill someone if you give extra information or anything else. \
        No explanation, no comments, no other text. \
        Please write ALL the code needed since it will be extracted directly and run from your response.\
        Always pd load the csv file name 'file.csv'\
        Always start the code with '''python and end with '''"""
    
    client = openai.OpenAI(
        api_key=os.environ.get("SAMBANOVA_API_KEY"),
        base_url="https://api.sambanova.ai/v1",
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role":"system","content":"You are a helpful assistant that generates working python code."},{"role":"user","content":user_input}],
        temperature =  0.1,
        top_p = 0.1
    )

    return response.choices[0].message.content, prompt


# call_snova("What is the capital of France?")



def call_snova_training_questions(df, model_name = "Meta-Llama-3.1-8B-Instruct", num_questions = 5):
    # print("model_name", model_name)
    # print("user_input", user_input)
    # print("df", df.columns.tolist())
    prompt = f"""Given the following dataset columns: {df.columns.tolist()}, \
    please generate a list of {num_questions} insightful training questions that can be asked about the dataset. \
    Ensure the questions are relevant and cover various aspects to visualize the data. Ask questions about bar chart, scatter plot, box plot, pie chart, etc. \
    Eg: 'Scatter Plot of Screen On Time vs. Battery Drain' \
        Output should be a list of questions in the following format: \
        ['Question 1', 'Question 2', 'Question 3', 'Question 4', 'Question 5', 'Question 6'...]
        start with [ and end with ] as a python list.
    """
    
    client = openai.OpenAI(
        api_key=os.environ.get("SAMBANOVA_API_KEY"),
        base_url="https://api.sambanova.ai/v1",
    )

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role":"system","content":"You are a helpful assistant that generates working training questions for the dataset visualization."},{"role":"user","content":prompt}],
        temperature =  0.1,
        top_p = 0.1
    )

    return response.choices[0].message.content, prompt
