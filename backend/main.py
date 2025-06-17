from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
import openai
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="HauntScript API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

class StoryRequest(BaseModel):
    theme: str
    length: Optional[str] = "medium"
    tone: Optional[str] = "dark"
    characters: Optional[list[str]] = None

class StoryResponse(BaseModel):
    title: str
    content: str
    generated_at: str

@app.get("/")
async def root():
    return {"message": "Welcome to HauntScript API"}

@app.post("/generate-story", response_model=StoryResponse)
async def generate_story(request: StoryRequest):
    try:
        # Construct the prompt
        prompt = f"Write a horror story with the following parameters:\n"
        prompt += f"Theme: {request.theme}\n"
        prompt += f"Length: {request.length}\n"
        prompt += f"Tone: {request.tone}\n"
        if request.characters:
            prompt += f"Characters: {', '.join(request.characters)}\n"
        
        # Generate story using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a horror story writer. Create engaging and terrifying narratives."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the generated story
        story_content = response.choices[0].message.content
        
        # Split into title and content
        lines = story_content.split('\n')
        title = lines[0].strip()
        content = '\n'.join(lines[1:]).strip()
        
        return StoryResponse(
            title=title,
            content=content,
            generated_at=datetime.now().isoformat()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 