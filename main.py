import google.generativeai as genai
import PIL.Image
import streamlit as st

# Configure Generative AI with API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def foodAnalyzing(animal_type, age, breed, mood, health_condition):
    st.title("Animal Food Analyzer")

    # File uploader for food image
    uploaded_file = st.file_uploader("Upload food image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the image using PIL
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption="Uploaded Food Image", use_column_width=True)

        # Use the generative AI model to analyze the food
        prompt = f"""
        You are an animal food analyzer.
        Analyze the food in the uploaded image for a {age}-year-old {breed} ({animal_type}).
        Mood: {mood}, Health Condition: {health_condition}.

        Provide the following:
        - List of food detected.
        - Whether the animal can eat each food item.
        """

        # Generate content using the generative AI model
        response = genai.generate_text(
            model="gemini-1.5-flash",
            prompt=prompt
        )

        # Display the result
        st.subheader("Identification Result")
        st.text(response.result)
    else:
        st.info("Please upload a food image to analyze.")

# Call the function with sample parameters
foodAnalyzing("Dog", "2", "Chihuahua", "Happy", "None")


# import openai
# import google.generativeai as genai
# import PIL.Image
# import streamlit as st

# genai.configure(api_key = st.secrets('GOOGLE_API_KEY'))

# def foodAnalyzing(Type, Age, Breed, Mood, Health_Condition):
#   st.title("Animal food analyzer")
#   food_path = st.file_uploader("Upload food image", type=["jpg", "jpeg", "png"])

#   if uploaded_file is not None:
#         # Open the image using PIL
#         image = PIL.Image.open(uploaded_file)

#         model = genai.GenerativeModel(
#             "gemini-1.5-flash",
#             system_instruction="""
#             You are an animal food analyzer. 
#             You will first analyze the food inside the uploaded image.
#             Then analyze whether the specific animal can eat the food or not.
#             You will list all the food in the image. The output will be in the format as shown below:
#             Food in the image: <food>

#             Analysis: <analysis of the can and cannot eat>
#             """
#         )

#         response = model.generate_content(["Identify whether the animal can eat the food.", image])
#         st.subheader("Identification Result")
#         st.text(response.text)

# foodAnalyzing("Dog", "2", "Chihuahua", "Happy", "None")