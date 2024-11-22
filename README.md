# Study Notes Generator from YouTube Videos
This project creates concise and focused summaries highlighting important points for university students' exam preparation by extracting text transcripts from YouTube videos. It helps identify key information that might appear in exams.

## Features
- Automatic transcript extraction from YouTube videos (English supported)
- Summarizes important points for exam study within 250 words
- Easy and user-friendly interface

## Requirements
You need the following requirements to run this project:
- **Python 3.8 or higher**
- Required libraries (installation instructions provided below)

## Installation
1. **Clone the project:**
    ```bash
    git clone https://github.com/canbingol/youtube_video_summarizer
    ```

2. Install required dependencies: Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Create Google AI Studio API Key:
    - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
    - Create an API Key for API access

4. Create .env file and add API key:
    - Create a .env file in the project directory
    - Add this line to the file:
    ```bash
    GOOGLE_API_KEY="ENTER_YOUR_API_KEY_HERE"
    ```

## Usage
To start the project, run the following command:
```bash
streamlit run app.py
```
In the interface that opens in your browser, enter the YouTube Video Link and click the "Get Notes" button.
The system will extract the transcript from the video and create a focused summary for exam study.

## Warnings
⚠️ **Customizable Prompt:**  
The prompt can be modified to create different types of summaries according to your needs.

⚠️ **Language Subtitle Requirement:**  
This application works only for YouTube videos with subtitles in your selected language. Summarization cannot be done for videos without subtitle support.

You can create summaries for videos in any language by changing the 'tr' part in the following code line to your desired language:
```bash
transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['your_video_language'])
```
