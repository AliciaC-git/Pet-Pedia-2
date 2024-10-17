import openai
import google.generativeai as genai
import PIL.Image
import streamlit as st

genai.configure(api_key = st.secrets('GOOGLE_API_KEY'))

def foodAnalyzing(Type, Age, Breed, Mood, Health_Condition):
  st.title("Animal food analyzer")
  food_path = st.file_uploader("Upload food image", type=["jpg", "jpeg", "png"])

  if uploaded_file is not None:
        # Open the image using PIL
        image = PIL.Image.open(uploaded_file)

        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction="""
            You are an animal food analyzer. 
            You will first analyze the food inside the uploaded image.
            Then analyze whether the specific animal can eat the food or not.
            You will list all the food in the image. The output will be in the format as shown below:
            Food in the image: <food>

            Analysis: <analysis of the can and cannot eat>
            """
        )

        response = model.generate_content(["Identify whether the animal can eat the food.", image])
        st.subheader("Identification Result")
        st.text(response.text)

foodAnalyzing("Dog", "2", "Chihuahua", "Happy", "None")