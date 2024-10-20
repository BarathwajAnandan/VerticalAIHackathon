import base64
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def analyze_image(image_path,question ):
    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    base64_image = encode_image(image_path)

    url = "https://api.aimlapi.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('API_KEY')}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": 
        [
            {
                "role": "user",
                "content": 
                [
                    {"type": "text", "text": f"Given an image of a plot, please tell me if the plot answers the question ONLY SAY YES OR NO: {question}"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post(url, headers=headers, json=payload)
    try:
        if response.json()["choices"][0]["message"]["content"] == "YES":
            return True
        else:
            return False
    except:
        print("Error in analyzing image")
        return False
    


# Usage example:
# result = analyze_image('/Users/barathwajanandan/Documents/ws/vertical_hackathon/png_files/plot_0e49bb31.png')
# print(result)
