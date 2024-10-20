import streamlit as st
import pandas as pd
import re
import uuid
import subprocess
import os 
import json
from datetime import datetime
from dotenv import load_dotenv
from curl_response import get_chat_completion
from snova import call_snova, call_snova_training_questions
from image_check import analyze_image
import shutil
from get_train_json import generate_final_json
# Load environment variables from .env file
load_dotenv()
# Title of the web app
FINISHED = False


st.title("DataGen - Automated Synthetic Data Generation Framework for Your Tasks")
st.markdown("<h3 style='font-size: 24px;'>Let's make smaller models useful! - powered by Sambanova, AIML API</h3>", unsafe_allow_html=True)

model_options = [
    "Meta-Llama-3.2-3B-Instruct",
    "Meta-Llama-3.2-1B-Instruct",
    "Meta-Llama-3.1-8B-Instruct",
    "Meta-Llama-3.1-405B-Instruct",
    "Meta-Llama-3.1-70B-Instruct",
]
generate_questions = st.radio("You choose: I can help you generate questions or you can bring your own questions", ("Please generate for me", "Nah, I already have a list of questions"), index=1) == "Please generate for me"

if generate_questions:
    num_questions = st.number_input("How many questions do you want to generate?", value=10, min_value=1, max_value=100)
CUSTOM_MODEL = st.radio("Use Custom Model 1B?", ("False", "True")) == "True"

if not CUSTOM_MODEL:
    model_name = st.selectbox("Please select a model from the following options:", model_options)
    if model_name not in model_options:
        print("Invalid model selected. Using default model.")
        model_name = model_options[0]  # Default to the first model
# model_name = "Meta-Llama-3.1-8B-Instruct"
# model_name = 'llama-3.2-1b-preview'

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_KEY2 = os.getenv("GROQ_API_KEY2")


# Radio button for training data generation vs inference
mode = st.radio("Select mode:", ("Training Data Generation", "Inference"))

# Add a button for fine-tuning instructions
if st.button("How to Fine-tune"):
    # Open the LLaMA-Factory GitHub repository in a new tab
    st.markdown(
        '<a href="https://github.com/hiyouga/LLaMA-Factory" target="_blank">Click here for fine-tuning instructions</a>',
        unsafe_allow_html=True
    )

#add buttons to open folders in streamlit 
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Open png_files"):
        os.system(f"open {os.path.join(os.getcwd(), 'png_files')}")

with col2:
    if st.button("Open code_files"):
        os.system(f"open {os.path.join(os.getcwd(), 'code_files')}")

with col3:
    if st.button("Open train_data"):
        os.system(f"open {os.path.join(os.getcwd(), 'train_data')}")

with col4:
    if st.button("Open wrong_files"):
        os.system(f"open {os.path.join(os.getcwd(), 'wrong_files')}")

with col5:
    if st.button("Open error_files"):
        os.system(f"open {os.path.join(os.getcwd(), 'error_files')}")

def extract_code_blocks(text):
    # print("line 25 text", type(text), text)
    # breakpoint()
    text = text.replace("Python", "")
    text = text.replace("python", "")
    # Regular expression pattern to find code blocks surrounded by triple backticks
    pattern = r"'''(.*)"
    pattern2 = r"(.*)'''"
    pattern_sub_1 =  r"```(.*)"
    pattern_sub_2 = r"(.*)```"
    # Using re.DOTALL to make the dot match newlines as well
    matches = re.findall(pattern, text, re.DOTALL)
    if not matches:
        matches = re.findall(pattern_sub_1, text, re.DOTALL)

        matches2 = re.findall(pattern_sub_2, matches[0], re.DOTALL)
    else:
        matches2 = re.findall(pattern2, matches[0], re.DOTALL)
    # 'matches' will be a list of all the code blocks found in the text
    return matches2

def create_python_file(response):
    global model_name
    code_blocks = extract_code_blocks(response)
    csv_file_path = uploaded_file.name
    filename = f"plot_{uuid.uuid4().hex[:8]}"
    if code_blocks:
        for block in code_blocks:
            print("Found code block:")
            code_block = block.strip()
            code_block_temp = code_block
            # code_block = code_block.replace("dataset.csv", csv_file_path)
            code_block = re.sub(r"'\w+\.csv'", f"'{csv_file_path}'", code_block)
            print("final code_block", code_block)
            
            # Append code_block to save the plot
            png_file_path = os.path.join("png_files", f"{filename}.png")
            code_block += f"\nplt.savefig('{png_file_path}')" 
    
    if code_block is not None:
        # Open the file in write mode ('w') which will overwrite the file if it already exists
        file_path = os.path.join("code_files", f"{filename}.py")
        with open(file_path, 'w') as file:
            file.write(code_block)
    else:
        print("No code block found in the response.")
    return file_path, code_block_temp

def get_input_questions():
    user_input_gpt = [
                # "Histogram of App Usage Time (min/day)",
                # "Bar Plot of Average App Usage Time by Device Model",
                "Scatter Plot of Screen On Time vs. Battery Drain",
                "Bar Plot of Number of Apps Installed by Operating System",
                # "Box Plot of Screen On Time by Gender",
                # "Correlation Heatmap of Numeric Features (App Usage, Screen On Time, Battery Drain, Data Usage, etc.)",
                # "Bar Plot of Average Data Usage by Age",
                # "Pie Chart of Device Model Distribution",
                # "Bar Plot of Average Battery Drain by User Behavior Class",
                # "Scatter Plot of Age vs. Screen On Time",
                # "Box Plot of Data Usage by Gender",
                # "Line Plot of Average App Usage Time by Age Group",
                # "Stacked Bar Plot of User Behavior Class by Operating System",
                # "Bar Plot of Average Screen On Time by Device Model",
                # "Density Plot of Battery Drain by Gender"
            ]
    for i in range(len(user_input_gpt)):
        user_input_gpt[i] = user_input_gpt[i].lower()

    return user_input_gpt

def generate_training_questions(df, num_questions):
    response, _ = call_snova_training_questions(df, model_name, num_questions)

    # breakpoint() 

    # Parse the response into a Python list using regex
    user_input_gpt = re.findall(r"'([^']*)'", response)
    
    print("user_input_gpt", user_input_gpt)

    return user_input_gpt


def main():
    global num_questions
    global FINISHED
    global model_name
    total_plots = 0
    correct_plots = 0
    # Check if a file has been uploaded
    if uploaded_file is not None and not FINISHED:
        # Read the file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        user_input = st.text_input("Prompt :")

        if mode == "Training Data Generation":
            if generate_questions:
                user_input_gpt = generate_training_questions(df, num_questions)
                # Save the output list to a new file
                output_filename = f"train_questions/training_questions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(output_filename, 'w') as f:
                    for question in user_input_gpt:
                        f.write(f"{question}\n")
                
            else:
                user_input_gpt = get_input_questions()
            
            #show the questions
            st.write("Here are the questions I will use to generate training data:")
            st.write(user_input_gpt)

            # Display the dataframe
            st.write("Columns in the dataset:")
            st.write("Here is a preview of the dataset:")
            st.write(df.head())
            # Display the columns in the dataset
            st.write(df.columns.tolist())

            for user_input in user_input_gpt:
                if FINISHED:
                    continue

                print("COLUMNS", df.columns.tolist())

                # text, prompt = groq_call(user_input, df)
                if CUSTOM_MODEL:
                    text,prompt = get_chat_completion(user_input, df)
                else:
                    text, prompt = call_snova(user_input, df, model_name)
                try:
                    file_path, code_temp = create_python_file(text)
                    skip = False
                    command = f"python {file_path}"
                    train_data = {"instruction": prompt,"input": "","output": code_temp}
                    base_path = os.path.basename(file_path)[:-3]
                    train_data_path = os.path.join("train_data", f"train_data_{base_path}.json")
                    if not os.path.exists("train_data"):
                        os.makedirs("train_data", exist_ok=True)
                    with open(train_data_path, 'w') as f:
                        json.dump(train_data, f)
                except:
                    skip = True
                    file_path = "None"
                    command = ""
                    train_data_path = ""
                if file_path:
                    result = subprocess.run(command, shell=True)
                    total_plots += 1
                    if result.returncode == 0 and not skip:
                        st.image(os.path.join("png_files",f"{base_path}.png"))
                        if analyze_image(os.path.join("png_files",f"{base_path}.png"), user_input):
                            st.write("AIML API powered by 4o says - GOOD JOB")
                            correct_plots += 1
                        else:
                            #save file to a different folder
                            os.rename(file_path, os.path.join("wrong_files", os.path.basename(file_path)))
                            st.write("AIML API powered by 4o says - BETTER LUCK NEXT TIME")
                            #copy image as well
                            shutil.copy(os.path.join("png_files",f"{base_path}.png"), os.path.join("wrong_files",f"{base_path}.png"))
                    else:
                        st.write("Error in running the code. Please try again. Files are moved to error_files folder")
                        
                        if os.path.exists(file_path):  # Check if the file exists
                            #move the file to a different folder
                            os.rename(file_path, os.path.join("error_files", os.path.basename(file_path)))
                            # os.remove(file_path)  # Remove the file if there is an error

                        if os.path.exists(train_data_path):
                            os.remove(train_data_path) # remove the train data if there is an error
                else:
                    st.write("No valid code block found to run.")
                
                # Display summary statistics
            st.write("Summary Statistics:")
            st.write(df.describe())
            st.write(f"Correct plots: {correct_plots}, Total plots: {total_plots}, Accuracy: {correct_plots*100/total_plots}%")
                    # Write correct plot accuracy and total plots to another json file called accuracy.json
            accuracy = {
                "csv_file_name": uploaded_file.name,       # Add the CSV file name
                "correct_plots": correct_plots,
                "total_plots": total_plots,
                "accuracy": correct_plots / total_plots,
                "questions_list": user_input_gpt,  # Add the questions list
                "groq_model": model_name
            }
            with open("accuracy.json", "a") as f:
                json.dump(accuracy, f)
                f.write("\n")  # Ensure each entry is on a new line
                
            #generate final json file with all the data
            #create a button to call a python script to generate the final json file
            
            # if st.button("Generate Final JSON File"):
                # FINISHED = True
            generate_final_json()
            st.write("Final JSON file generated successfully and saved to identity.json")

                # uploaded_file = None
        
        
        else:  # Inference mode

            if user_input:
                st.write("Here is a preview of the dataset:")
                st.write(df.head())

                # Display the columns in the dataset
                st.write("Columns in the dataset:")
                st.write(df.columns.tolist())
                # text, prompt = groq_call(user_input, df)
                if CUSTOM_MODEL:
                    text, prompt = get_chat_completion(user_input, df)
                else:
                    text, prompt = call_snova(user_input, df, model_name)
                file_path, code_temp = create_python_file(text)
                base_path = os.path.basename(file_path)[:-3]

                command = f"python {file_path}"
                if file_path:
                    result = subprocess.run(command, shell=True)
                    total_plots += 1
                    if result.returncode == 0:
                        st.image(os.path.join("png_files",f"{base_path}.png"))
                        correct_plots += 1
                    else:
                        st.write("Error in running the code. Please try again.")
                        os.remove(file_path) # remove the file if there is an error
                else:
                    st.write("No valid code block found to run.")
                
                # Display summary statistics
                st.write("Summary Statistics:")
                st.write(df.describe())
        


if __name__ == "__main__":
    main()
