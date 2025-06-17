import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import streamlit_lottie

# Load environment variables from .env file
load_dotenv()

# --- Gemini Pro API Key Configuration ---
# You can set your API key here directly or use an environment variable for security
# Example: os.environ['GOOGLE_API_KEY'] = 'your-api-key-here'
genai.configure(api_key=os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY_HERE"))

# --- Model Configuration ---
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# --- Horror Story Generation Function ---
def generate_horror_story(character_name, situation, no_of_lines):
    prompt = (
        f"You are a master of horror fiction. Write a chilling, atmospheric horror story.\n"
        f"Main character: {character_name}\n"
        f"Setting: {situation}\n"
        f"Length: {no_of_lines} lines\n"
        f"Include suspenseful build-up, vivid descriptions, and a twist ending. Use immersive, sensory language."
    )
    response = model.generate_content([prompt])
    return response.text

# --- Streamlit UI ---
def main():
    st.title("Horror Story Generator")
    st.write("Enter the details below to generate your custom horror story:")

    character_name = st.text_input("Character Name")
    situation = st.text_input("Situation")
    no_of_lines = st.number_input("Number of Lines", min_value=1)

    if st.button("Generate Story"):
        with st.spinner("Summoning the spirits of horror..."):
            try:
                story = generate_horror_story(character_name, situation, no_of_lines)
                st.subheader("Your Horror Story:")
                st.markdown(f"<div style='font-family: Creepster, serif; font-size: 1.2em; color: #e63946;'>{story.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
                st.download_button(
                    label="Download as TXT",
                    data=story,
                    file_name="horror_story.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 