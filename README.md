# Horror Story Generator

A spine-chilling web application that generates custom horror stories using Google's Gemini AI model. This application allows users to create unique horror narratives by specifying character names, situations, and desired story length.

## Features

- 🤖 Powered by Google's Gemini 1.5 Flash AI model
- 📝 Customizable story parameters:
  - Character name
  - Situation/setting
  - Story length
- 🎨 Atmospheric UI with horror-themed styling
- 💾 Download generated stories as text files
- 🔒 Secure API key management using environment variables

## Prerequisites

- Python 3.7 or higher
- Google Cloud account with Gemini API access
- Streamlit

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd horror-story-generator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run horror.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter the following details:
   - Character Name: The protagonist of your horror story
   - Situation: The setting or scenario for your story
   - Number of Lines: Desired length of the story

4. Click "Generate Story" to create your custom horror narrative

5. Download the generated story using the "Download as TXT" button

## Technical Details

### Dependencies
- streamlit: Web application framework
- google-generativeai: Google's Gemini AI API client
- python-dotenv: Environment variable management
- streamlit-lottie: Animation support

### Configuration
The application uses the following configuration for the Gemini model:
- Temperature: 0.9 (creativity level)
- Top P: 1
- Top K: 1
- Max Output Tokens: 2048
- Response MIME Type: text/plain

## Security Notes

- Never commit your API key to version control
- Always use environment variables for sensitive information
- Keep your `.env` file in `.gitignore`

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for providing the powerful language model
- Streamlit for the web application framework
- All contributors and users of this project 