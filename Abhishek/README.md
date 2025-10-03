# Gemini Multi-Image Editing Demo

This project shows how to use the **Gemini API** with Python to perform multi-image editing tasks.  
In this demo, we take an image of a man and a t-shirt, then generate an output image where the man is wearing the t-shirt — while keeping the background unchanged.

## Tech Stack
- **Cursor** (IDE)
- **Python**
- **Gemini API** (`google-genai`)
- **PIL** for image processing
- **python-dotenv** for environment variables

## How It Works
1. Load your API key from a `.env` file
2. Open two input images: `man.png` and `tshirt.png`
3. Send a prompt + images to the Gemini API
4. Save the output as `man-with-tshirt.png`

## Setup

### 1. Clone this repo
```bash
git clone https://github.com/yourusername/gemini-multi-image-demo.git
cd gemini-multi-image-demo
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file
```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Add input images
Place `man.png` and `tshirt.png` in the project folder.

### 5. Run the script
```bash
python main.py
```

## Output
The script will generate:
```
man-with-tshirt.png
```

## Notes
- Do **not** upload your real `.env` file to GitHub
- Replace the input images with your own for different results

## License
This project is for educational/demo purposes only.
