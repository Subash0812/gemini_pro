import os 
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import streamlit as st

load_dotenv()

genai.configure(api_key='AIzaSyB4FVj_0URVvuCQspEQRVJE3OJwH-UHptE')

def get_gemini_response(input_prompt,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
    

st.set_page_config(page_title="Health App")

st.header(":orange[Dr. Maddesan's Health App]")
st.write("### :green[You can upload your meal pic and get a calories split up and suggestions]")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
,tell this food is good for health are not and also mention the precentage split of the ratio of carbohydrates,fats,
fibers,sugar and other important things required in our diet.

"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)




# langchain
# PyPDF2
# chromadb
# pdf2image
# faiss-cpu
# langchain_google_genai
