from dotenv import load_dotenv
from google import genai
from PIL import Image
from io import BytesIO
import os

# Load .env file
load_dotenv()

# Configure the client with your API key
api_key = os.getenv("GOOGLE_API_KEY")  # matches your .env

client = genai.Client(api_key=api_key)

prompt = "Make the Man wear this t-shirt. Leave the background unchanged."

image1 = Image.open("man.png")
image2 = Image.open("tshirt.png")

response = client.models.generate_content(
    model="gemini-2.5-flash-image-preview",
    contents=[prompt, image1, image2],
)

# The response can contain both text and image data.
# Iterate through the parts to find and save the image.
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("Man_with_tshirt.png")
